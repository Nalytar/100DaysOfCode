import tkinter as tk


def calculate():
    try:
        uInput = userInput.get()
        uInput = str.replace(uInput, ",", ".", 1)
        uInput = float(uInput) * 1.609344
        labelKmNumber.config(text=uInput)

    except ValueError:
        labelKmNumber.config(text="Wrong input, please just insert a number")


window = tk.Tk()
# window.minsize(width=200, height=200)
window.title("Miles to Km Converter")
window.config(padx=50, pady=50)


userInput = tk.Entry()
userInput.config(width=40)
userInput.grid(column=1, row=0)

labelMiles = tk.Label(text="Miles")
labelMiles.grid(column=2, row=0)

labelKM = tk.Label(text="Km")
labelKM.grid(column=2, row=1)

labelKmNumber = tk.Label(text="0")
labelKmNumber.grid(column=1, row=1)

textLabel = tk.Label(text="is equal to")
textLabel.grid(column=0, row=1)

calcButton = tk.Button(command=calculate, text="Calculate")
calcButton.grid(column=1, row=2)

window.mainloop()
