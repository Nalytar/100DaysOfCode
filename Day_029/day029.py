# udemy Course - 100 Days of Code - Python
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

BACKGROUND = "white"


def generatePassword():
	letters = string.ascii_letters
	numbers = string.digits
	symbols = string.punctuation

	nr_letters = random.randint(8, 10)
	nr_numbers = random.randint(2, 4)
	nr_symbols = random.randint(2, 4)

	password = []

	for _ in range(nr_letters):
		password.append(random.choice(letters))

	for _ in range(nr_numbers):
		password.append(random.choice(numbers))

	for _ in range(nr_symbols):
		password.append(random.choice(symbols))

	random.shuffle(password)
	password = "".join(password)
	pyperclip.copy(password)

	if len(pwInput.get()) > 0:
		pwInput.delete(0, tk.END)
	pwInput.insert(0, password)


def validate(service, user, pw):
	lenService = len(service)
	lenUser = len(user)
	lenPw = len(pw)
	if lenPw > 0 and lenUser > 0 and lenService > 0:
		return True
	return False


def save():
	service = serviceInput.get()
	user = userInput.get()
	pw = pwInput.get()
	combi = ("-------------------------------------------------------------------------\n\n" +
			 "-- " + service + " --\nUsername/E-Mail: " + user + "\nPassword: " + pw + "\n\n")

	if not validate(service, user, pw):
		messagebox.showerror("ERROR", "There are empty inputs!")
		return

	if messagebox.askokcancel(service, f"Your inputs:\nEmail/User: {user}\nPassword: {pw}\nOk to safe?"):
		with open("manager.txt", "a") as file:
			file.write(combi)
			serviceInput.delete(0, tk.END)
			pwInput.delete(0, tk.END)


window = tk.Tk()
window.title("Password-Manager")
window.config(pady=52, padx=52, background=BACKGROUND)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0, background=BACKGROUND)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

serviceLabel = tk.Label()
serviceLabel.config(text="Website:", background=BACKGROUND)
serviceLabel.grid(column=0, row=1)

serviceInput = tk.Entry(width=52)
serviceInput.grid(column=1, row=1, columnspan=2)
serviceInput.focus()

userLabel = tk.Label()
userLabel.config(text="User/E-Mail:", background=BACKGROUND)
userLabel.grid(column=0, row=2)

userInput = tk.Entry(width=52)
userInput.grid(column=1, row=2, columnspan=2)
userInput.insert(0, "kelle.michael@web.de")

pwLabel = tk.Label()
pwLabel.config(text="Password:", background=BACKGROUND)
pwLabel.grid(column=0, row=3)

pwInput = tk.Entry(width=33)
pwInput.grid(column=1, row=3)

genButton = tk.Button()
genButton.config(text="Generate Password", background=BACKGROUND, command=generatePassword)
genButton.grid(column=2, row=3)

saveButton = tk.Button()
saveButton.config(text="Add", background=BACKGROUND, width=43, command=save)
saveButton.grid(column=1, row=4, columnspan=2)

window.mainloop()
