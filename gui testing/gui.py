from tkinter import *

root = Tk(className="Speech to C Code Framework")
root.geometry("1920x1080")

label = Label(root, text="Hello, world!")
label.pack()

t1 = Text(root, height = 50, width = 100)
t1.pack(padx=10, side=LEFT)

t2 = Text(root, height = 50, width = 150)
t2.pack(side=LEFT)

active = 1
while active:
    root.update()
    voiceInput = input("Enter text [exit to terminate]: ")
    f1 = open("some_random_file.txt", "r")
    codeInput = f1.read()
    f1.close()
    if voiceInput == "exit":
        root.quit()
        text = t2.get("1.0", "end-1c")  
        print("####################")
        print("Contents")
        print("####################")
        print(text)

        # Writing to output file 
        outputFile = open("outputCode.c", "w")
        outputFile.write(text)
        outputFile.close()
        active = 0
    else:
        voiceInput+="\n"
        t1.insert(END, voiceInput)
        t1.pack()
        t2.insert(END, codeInput)
        t2.pack()