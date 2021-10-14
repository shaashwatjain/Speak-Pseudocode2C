import time
from tkinter import *
from tkinter import ttk

root = Tk(className="Speech to C Code Framework")
root.geometry("1920x1080")

t1 = Text(root, height = 50, width = 100)
t1.pack(padx=10, side=LEFT)
t2 = Text(root, height = 50, width = 150)
t2.pack(side=LEFT)


f1 = open("pseudocode/area_perimeter.txt", "r")
voiceInput = f1.readlines()
f1.close()
print("transcript:", voiceInput)

f2 = open("codes/area_perimeter.txt", "r")
codeInput = f2.read()
f2.close()
for i in voiceInput:
    root.update()

    if "start" in i or "begin" in i:
        t1.insert(END, i)
        t1.pack()
        t2.insert(END, "/* starting the code */\n")
        t2.pack()
    elif "exit" in i or "end" in i:
        t1.insert(END, i)
        t1.pack()
        t2.insert(END, "\n/* code completed */")
        t2.pack()
        root.update()
        time.sleep(5)

        root.quit()
        text = t2.get("1.0", "end-1c")
        outputFile = open("outputCode.c", "w")
        outputFile.write(text)
        outputFile.close()
    else:
        t1.insert(END, i)
        t1.pack()
        t2.insert(END, codeInput)
        t2.pack()
        time.sleep(1)
    time.sleep(1)
