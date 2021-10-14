import os
import sys
import time

from tkinter import *
from tkinter import ttk

#  from Google_Speech_to_text import *
#  from mapper import *


class Pseudocode2c:
    def __init__(self):
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

        self.undo_button = Button(self.Frame, text="Undo")
        self.undo_button.configure(height=3, width=10)
        self.undo_button.place(x=1350, y=55)

        left_text = Text(self.Frame, relief=GROOVE, height=40, width=100, borderwidth=2)
        left_text.pack(padx=80, side=LEFT)
        right_text = Text( self.Frame, relief=GROOVE, height=40, width=100, borderwidth=2)
        right_text.pack(side=LEFT)

        self.compile_button = Button(self.Frame, text="compile the program")
        self.compile_button.configure(height=3)
        self.compile_button.place(x=400, y=850)

        self.exit_button = Button(self.Frame, text="exit the Framework")
        self.exit_button.configure(height=3)
        self.exit_button.place(x=1320, y=850)

        root.mainloop()

    def run_framework():
        file = open("transcript.txt", "r")
        while last_line.strip() == "":
            continue

        # send last line to mapper
        last_line = list(file.read().splitlines())[-1]


if __name__ == "__main__":
    run = Pseudocode2c()
