from tkinter import *

def hello_world():
  print("Hello, world!")

root = Tk()
root.title("Hello World!")

button = Button(root, text="Click me!", command=hello_world)
button.pack()

root.mainloop()
