import tkinter as tk

def display_message():
    label.config(text="Hello, World!")

# Create the main window
root = tk.Tk()
root.title("Hello World GUI")

# Create a label widget to display the message
label = tk.Label(root, text="")
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me", command=display_message)
button.pack()

# Run the application
root.mainloop()
