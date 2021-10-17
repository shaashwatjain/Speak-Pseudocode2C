import re

import wordtodigits
from google.cloud import speech_v1p1beta1 as speech

from corrections import corr_list
from exceptions import SpeechToTextException
from mapper import Mapper
from speech_to_text import (MicrophoneStream, post_indentation, pre_indentation, replacement)

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


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
    mapper_obj = Mapper()
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        if result.is_final:
            if transcript[0] == " ":
                transcript = transcript[1:]
                transcript += " "
            try:
                transcript = wordtodigits.convert(transcript)
                transcript = transcript.lower()
                transcript = replacement(transcript)
                indent = pre_indentation(transcript, indent)

                # LEFT
                resultant = "\t"*indent + transcript
                #Nedd to have a fn call to add text in lhs

                # RIGHT
                list_for_program = mapper_obj.process_input(resultant)
                len_source_code = len(list_for_program)
                # Need to have a fn call to rhs and pass len_source_code
                for line in list_for_program:
                    print(line, end="")

                indent = post_indentation(transcript, indent)
            except:
                print("Conversion failed")
                raise SpeechToTextException

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break


def InitializeStream():
    language_code = "en-IN"  # a BCP-47 language tag

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

        listen_print_loop(responses)


InitializeStream()
