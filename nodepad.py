from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
root.geometry("624x575")
root.title("MyNotepad")
# def F1():
#     print("Hi there Its me Notepad")

def quitt():
    print(quit())

def Myself():
    print("Hey There Its Me Md Tausif\nAnd This is a simple Notepad\nMyNotepad is my first software")


def newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    text.delete(1.0,END)




def openfile():

    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text document","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()




def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                               filetypes=[("All files","*.*"),("Text document","*.txt")])
        if file=="":
            file=None

        else:
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("File is Saved")
    else:
        #save the file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()




def saveasfile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All files", "*.*"), ("Text document", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("File is Saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()


Mainmenu = Menu(root)
m1 = Menu(Mainmenu,tearoff=0)
m1.add_command(label="New          Ctrl+N",command = newfile)
m1.add_command(label="Open         Ctrl+O",command = openfile)
m1.add_command(label="Save          Ctrl+S",command = savefile)
m1.add_command(label="Save As       Ctrl+Alt+S",command = saveasfile)
m1.add_separator()
m1.add_command(label="Exit",command = quitt)
Mainmenu.add_cascade(label="File",menu=m1)

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))




m2 = Menu(Mainmenu,tearoff=0)
m2.add_command(label="Cut     Ctrl+X",command = cut)
m2.add_command(label="Copy    Ctrl+C",command = copy)
m2.add_command(label="Paste    Ctrl+V",command = paste)
Mainmenu.add_cascade(label="Edit",menu=m2)

def helpme():
    showinfo("Notepad","Notepad By Chaudhuri Md Tausif")


m3 = Menu(Mainmenu,tearoff=0)
m3.add_command(label="Help     Ctrl+H",command = helpme)
m3.add_command(label="About    ",command = Myself)
Mainmenu.add_cascade(label="Help",menu=m3)


text = Text(root,font = "arial 12")
file = None
text.pack(expand=True,fill=BOTH)

Scroll = Scrollbar(text)
Scroll.pack(side=RIGHT,fill= Y)
Scroll.config(command=text.yview )
text.config(yscrollcommand=Scroll.set)

root.config(menu=Mainmenu)
root.mainloop()
