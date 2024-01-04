from tkinter import *

root = Tk()
mylablel1 = Label(root, text="Hello World!")
mylablel2 = Label(root, text="My name is John Elder")

def clickmefun():
    mylablel2['text'] = "You clicked the button!"

Button = Button(root, text="Click Me!", command=clickmefun, fg="blue", bg="red")

mylablel1.grid(row=0, column=1)
mylablel2.grid(row=1, column=2)
mylablel2.grid(row=2, column=2)

root.mainloop()
