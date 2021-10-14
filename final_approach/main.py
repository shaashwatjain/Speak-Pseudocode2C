import os
import sys
import time
import subprocess

from tkinter import *
from tkinter import ttk

#  from Google_Speech_to_text import *
#  from mapper import *


class Pseudocode2c:
    def __init__(self):
        self.path = os.getcwd()

        self.output_dir = self.path + "\\Output"
        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)
        self.file_name = self.output_dir + "\\Sample_code.c"

        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#ffffff"  # X11 color: 'white'
        _ana1color = "#ffffff"  # X11 color: 'white'
        _ana2color = "#ffffff"  # X11 color: 'white'
        font14 = (
            "-family {Segoe UI} -size 15 -weight bold -slant "
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

        root = Tk()
        root.geometry("1920x1080")
        root.title("Speak Pseudocode2c: A framework to convert pseudocode to c code")
        root.configure(background="#fafafa")
        root.configure(highlightbackground="#c8e6c9")
        root.configure(highlightcolor="black")

        self.menubar = Menu(root, font=font9, bg=_bgcolor, fg=_fgcolor)
        root.configure(menu=self.menubar)

        self.Frame = Frame(root)
        self.Frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame.configure(
            borderwidth="2",
            relief=GROOVE,
            background="#d9d9d9",
            highlightbackground="#d9d9d9",
            highlightcolor="black",
            width=925,
        )

        self.start_button = Button(self.Frame, text="Start the Framework")
        self.start_button.configure(height=3)
        self.start_button.place(x=420, y=50)

        self.undo_button = Button(self.Frame, text="Undo", command=lambda:self.remove_junk(2))
        self.undo_button.configure(height=3, width=10)
        self.undo_button.place(x=1350, y=55)

        self.left_text = Text(
            self.Frame, relief=GROOVE, height=40, width=100, borderwidth=2
        )
        self.left_text.pack(padx=80, side=LEFT)
        self.right_text = Text(
            self.Frame, relief=GROOVE, height=40, width=100, borderwidth=2
        )
        self.right_text.pack(side=LEFT)

        self.compile_button = Button(
            self.Frame, text="compile the program", command=self.compile_program
        )
        self.compile_button.configure(height=3)
        self.compile_button.place(x=400, y=850)

        self.exit_button = Button(
            self.Frame, text="Save and exit", command=self.save_code
        )
        self.exit_button.configure(height=3)
        self.exit_button.place(x=1320, y=850)

        root.mainloop()

    def save_code(self):
        text_to_write = self.right_text.get("1.0", "end-1c")
        outputFile = open(self.file_name, "w")
        outputFile.write(text_to_write)
        outputFile.close()

    def compile_program(self):
        os.chdir(self.output_dir)
        os.system("gcc {0} -o out && out.exe".format(self.file_name))

        ####################
        # Using subprocess #
        ####################
        #  subprocess.check_call("gcc Sample_code.c -o out1", shell = True)
        #  s = subprocess.check_call("out1.exe", shell = True)
        #  print(", return code", s)

    def remove_junk(self, count):
        num_lines_to_delete = "end-{0}l".format(count + 1)
        self.right_text.delete(num_lines_to_delete, "end")


if __name__ == "__main__":
    run = Pseudocode2c()
