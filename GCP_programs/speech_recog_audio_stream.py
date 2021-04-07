from __future__ import division

import re
import sys
import os
from corrections import corr_list
from word2number import w2n
import wordtodigits

#  from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech

import pyaudio
from six.moves import queue

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

def pre_indentation(transcript,indent):
    dec_indent = ["end","else"]
    for inc in dec_indent:
        if inc in transcript:
            return indent - 1
    return indent

def post_indentation(transcript,indent):
    inc_indent = ["start","procedure","while","if","for","else"]
    for inc in inc_indent:
        if inc in transcript and "end" not in transcript:
            return indent + 1
    return indent

def replacement(string1):
    repl_dict = {
        "is equal to":"=",
        "equals to":"=",
        "is not equal to":"!=",
        "not equal to":"!=",
        "not equals":"!=",
        "not equal":"!=",
        "is not":"!=",
        "addition":"+",
        "add":"+",
        "plus":"+",
        "subtract":"-",
        "minus":"-",
        "multiplied by":"*",
        "multiply by":"*",
        "multiply":"*",
        "into":"*",
        " x ":"*",
        "divided by":"/",
        "divide by":"/",
        "divide":"/",
        "modulo":"%",
        "mod":"%"
    }
    for key in repl_dict.keys():
        string1 = string1.replace(key,repl_dict[key])
    return(string1)


def is_number(x):
    if type(x) == str:
        x = x.replace(",", "")
    try:
        float(x)
    except:
        return False
    return True


def text2int(textnum, numwords={}):
    units = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    ordinal_words = {
        "first"   : 1,
        "second"  : 2,
        "third"   : 3,
        "fifth"   : 5,
        "eighth"  : 8,
        "ninth"   : 9,
        "twelfth" : 12,
    }
    ordinal_endings = [("ieth", "y"), ("th", "")]

    if not numwords:
        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace("-", " ")

    current = result = 0
    curstring = ""
    onnumber = False
    lastunit = False
    lastscale = False

    def is_numword(x):
        if is_number(x):
            return True
        if word in numwords:
            return True
        return False

    def from_numword(x):
        if is_number(x):
            scale = 0
            increment = int(x.replace(",", ""))
            return scale, increment
        return numwords[x]

    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
            lastunit = False
            lastscale = False
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[: -len(ending)], replacement)

            if (not is_numword(word)) or (word == "and" and not lastscale):
                if onnumber:
                    # Flush the current number we are building
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
                lastunit = False
                lastscale = False
            else:
                scale, increment = from_numword(word)
                onnumber = True

                if lastunit and (word not in scales):
                    # Assume this is part of a string of individual numbers to
                    # be flushed, such as a zipcode "one two three four five"
                    curstring += repr(result + current)
                    result = current = 0

                if scale > 1:
                    current = max(1, current)

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0

                lastscale = False
                lastunit = False
                if word in scales:
                    lastscale = True
                elif word in units:
                    lastunit = True

    if onnumber:
        curstring += repr(result + current)

    return curstring


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    indent = 0
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript
        #print(transcript)

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        #overwrite_chars = " " * (num_chars_printed - len(transcript))

        if result.is_final:
            if transcript[0] == " ":
                transcript = transcript[1:]
                transcript += " "
            # print(transcript + overwrite_chars)
            # print(transcript + overwrite_chars)
            # try:
            #     print(w2n.word_to_num(transcript + overwrite_chars))
            # except:
            #     print("First failed")
            # try:
            #     print(text2int(transcript + overwrite_chars))
            # except:
            #     print("Second failed")
            try:
                transcript = wordtodigits.convert(transcript)
                transcript = replacement(transcript)
                indent = pre_indentation(transcript,indent)
                print("    "*indent+transcript)
                file1 = open("transcript.txt", "a")
                file1.write("    "*indent + transcript + "\n")
                file1.close()
                indent = post_indentation(transcript,indent)
            except:
                print("Conversion failed")

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            num_chars_printed = 0


def main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = "en-IN"  # a BCP-47 language tag
    file2 = open("transcript.txt", "w")
    file2.close()

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
        speech_contexts=[{"phrases": corr_list, "boost": 20.0}],
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)


if __name__ == "__main__":
    main()
