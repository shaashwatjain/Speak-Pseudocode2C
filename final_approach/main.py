import multiprocessing
import os
import re
import subprocess
import sys
import threading
import time
from tkinter import *
from tkinter import messagebox, ttk

import wordtodigits
from google.cloud import speech_v1p1beta1 as speech

from corrections import corr_list
from exceptions import SpeechToTextException
from mapper import Mapper
from speech_to_text import ( MicrophoneStream, post_indentation, pre_indentation, replacement)

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class Pseudocode2c(threading.Thread):
    def __init__(self):
        self.path = os.getcwd()
        self.alive = True
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.output_dir = self.path + "\\Output"
        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)

        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#ffffff"  # X11 color: 'white'
        _ana1color = "#ffffff"  # X11 color: 'white'
        _ana2color = "#ffffff"  # X11 color: 'white'
        font14 = (
            "-family {Segoe UI} -size 15 -weight normal -slant "
            "roman -underline 0 -overstrike 0"
        )
        font16 = (
            "-family {Swis721 BlkCn BT} -size 40 -weight bold "
            "-slant roman -underline 0 -overstrike 0"
        )
        font9 = (
            "-family {Segoe UI} -size 9 -weight normal -slant "
            "roman -underline 0 -overstrike 0"
        )

        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title(
            "Speak Pseudocode2c: A framework to convert pseudocode to c code"
        )
        self.root.configure(background="#fafafa")
        self.root.configure(highlightbackground="#c8e6c9")
        self.root.configure(highlightcolor="black")

        self.menubar = Menu(self.root, font=font9, bg=_bgcolor, fg=_fgcolor)
        self.root.configure(menu=self.menubar)

        self.Frame = Frame(self.root)
        self.Frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame.configure(
            borderwidth="2",
            relief=GROOVE,
            background="#d9d9d9",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
        )

        self.start_button = Button(self.Frame, text="Start the Framework", default=DISABLED)
        self.start_button.configure(height=3)
        self.start_button.place(relx = 0.18, rely = 0.02)

        self.undo_button = Button(
            self.Frame, text="Undo", command=lambda: self.remove_junk()
        )
        self.undo_button.configure(height=3, width=10)
        self.undo_button.place(relx = 0.72, rely = 0.02)

        self.lines_to_delete = []

        Label(self.Frame, text = "Spoken Pseudocode").place(relx = 0.025, rely = 0.08, relheight=0.05, relwidth=0.12)
        Label(self.Frame, text = "Converted C Code").place(relx = 0.525, rely = 0.08, relheight=0.05, relwidth=0.12)

        self.left_text = Text(
            self.Frame, relief=GROOVE, borderwidth=2
        )
        self.left_text.place(relx = 0.025, rely = 0.125, relheight=0.75, relwidth=0.475)
        self.left_text.configure(font=font14)
        # self.left_text.pack(side=LEFT)

        self.right_text = Text(
            self.Frame, relief=GROOVE, borderwidth=2
        )
        self.right_text.place(relx = 0.525, rely = 0.125, relheight=0.75, relwidth=0.45)
        self.right_text.configure(font=font14)
        # self.right_text.pack(side=RIGHT)

        self.compile_button = Button(
            self.Frame, text="compile the program", command=self.compile_program
        )
        self.compile_button.configure(height=3)
        self.compile_button.place(relx = 0.18, rely = 0.9)

        self.file_name = Text(
            self.Frame, relief=GROOVE, height=1, width=20, borderwidth=1
        )
        self.file_name.place(relx = 0.6, rely = 0.925)

        self.save_button = Button(
            self.Frame, text="Save the Program", command=self.save_code
        )
        self.save_button.configure(height=3)
        self.save_button.place(relx = 0.7, rely = 0.9)

        self.exit_button = Button(
            self.Frame, text="Exit the Program", command=self.exit_code
        )
        self.exit_button.configure(height=3)
        self.exit_button.place(relx = 0.85, rely = 0.9)

        self.root.mainloop()

    def save_code(self):
        text_to_write = self.right_text.get("1.0", "end-1c")
        self.file_name = self.file_name.get("1.0", "end-1c")
        if self.file_name == "":
            self.file_name = "SampleCode.c"
        self.file_path = self.output_dir + "\\" + self.file_name
        outputFile = open(self.file_path, "w")
        print("file saved as", self.file_path)
        outputFile.write(text_to_write)
        outputFile.close()

    def compile_program(self):
        os.chdir(self.output_dir)
        os.system("gcc {0} -o out && out.exe".format(self.file_name))

    def remove_junk(self):
        num_lines_to_delete = "end-{0}l".format(self.lines_to_delete.pop() + 1)
        self.right_text.delete(num_lines_to_delete, "end")
        self.left_text.delete("end-2l", "end")
        self.insert_lhs("\n")
        self.insert_rhs("\n")

    def exit_code(self):
        self.alive = False
        self.root.destroy()
        sys.exit(0)

    def insert_lhs(self, text_to_write):
        self.left_text.insert("end", text_to_write)

    def insert_rhs(self, text_to_write):
        self.right_text.insert("end", text_to_write)

    def show_alert(self, text_to_write):
        messagebox.showerror(
            title="Exception", message="Oops! {0} occured".format(text_to_write)
        )


def listen_print_loop(responses, obj):
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
    flag = 1
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

            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                flag = 0
                if not gui.alive:
                    sys.exit(0)
            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.

            try:
                transcript = wordtodigits.convert(transcript)
                transcript = transcript.lower()
                transcript = replacement(transcript)
                indent = pre_indentation(transcript, indent)

                # LEFT
                if flag:
                    resultant = "\t" * indent + transcript
                else:
                    resultant = "exit pseudocode"
                obj.insert_lhs(resultant + "\n")
                # Nedd to have a fn call to add text in lhs

                # RIGHT
                list_for_program = mapper_obj.process_input(resultant)
                len_source_code = len(list_for_program)
                # Need to have a fn call to rhs and pass len_source_code
                obj.lines_to_delete.append(len(list_for_program))
                for line in list_for_program:
                    print(line, end="")
                    obj.insert_rhs(line)
                indent = post_indentation(transcript, indent)

            except:
                # print("Conversion failed")
                obj.show_alert(sys.exc_info()[0])
                #  raise SpeechToTextException

        if not flag:
            break


def InitializeStream(obj):
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

        listen_print_loop(responses, obj)


if __name__ == "__main__":
    gui = Pseudocode2c()
    print("Running Google Speech to text...")
    InitializeStream(gui)
