# udemy Course - 100 Days of Code - Python
# GUI - https://docs.python.org/3/library/tk.html

import tkinter as tk
FONT = ("courier", 18, "normal")


window = tk.Tk()
window.title("My First GUI Program in Python")
window.minsize(width=1024, height=768)
window.config(padx=10, pady=10)


# Label
my_label = tk.Label(text="I Am a Label", font=FONT)
my_label.grid(column=0, row=0)  # Place in into the Screen and automatically center it, takes a conf dict as argument

# replace the "config"
my_label["text"] = "new Labeltext"
my_label.config(text="new Labeltext 2.0")

# Button


# def button_clicked():
#     print("I got clicked")
# def button_clicked():
#     my_label.config(text="I got clicked")
def button_clicked():
    my_label.config(text=userInput.get())


button = tk.Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

newButton = tk.Button(text="New Button!")
newButton.grid(column=2, row=0)

# Exercise On a button click change text of the defined label
# See line 25


# Entry
userInput = tk.Entry()
userInput.config(width=30)
# userInput.pack()
userInput.grid(column=3, row=3)

# use place, pack or grid to add Elements
# pack just place it on the side thats specified
# place must be very specific with x and y value
# grid you specify with

window.mainloop()
