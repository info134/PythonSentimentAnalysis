import threading
from tkinter import ttk
from tryyy import *
from DataTrain import *
from tkinter import *


root = Tk()
ax = threading.Thread(target=Parse().runMe).start()

label = ttk.Label(root, text = 'Instructions: type in a sentence or word in the box under to see if it is positive or negative. Then click "Submit".\nFor a more verbose '
                               'output consult the console log')
label.pack()

button = ttk.Button(root, text = "Submit - check console log that parsing finished")
button.pack()
a = Parse()



entry = ttk.Entry(root, width=100)
entry.pack()
entry.insert(0, 'This is an example sentence')

def f():

    print ('Sentence: ', entry.get())
    if Calculate.naive_bayes(entry.get(),entry.get())== "f":
        root.config(bg = 'red')
        label.config(font=("Ariel", 55), text = "Negative input")
    elif Calculate.naive_bayes(entry.get(),entry.get())== "t":
        root.config(bg = 'green')
        label.config(font=("Ariel", 55), text="Positive input")
    elif Calculate.naive_bayes(entry.get(),entry.get())== "e":
        root.config(bg = 'yellow')
        label.config(font=("Ariel", 55), text="Neutral input")

def clear():
    root.config(bg='white')
    label.config(text="")
    entry.delete(0,500)



########### combobox
button2 = ttk.Button(root, text = "Clear results", command= clear)
button2.pack()

label = Label(root)
label.pack()
print (threading.enumerate())



button.config(command = f)
button = Button (root, text = "Exit", command = root.destroy)
button.pack()
#
# while(True):
#     def ny():
#         if not (ax.isAlive()):
#             button.config(text="Submit", state="normal")
# axx = threading.Thread(target=ny).start()
root.mainloop()


