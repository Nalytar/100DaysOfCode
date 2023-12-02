# udemy Course - 100 Days of Code - Python
import encodings.utf_8
import tkinter as tk
import pandas as pd
import random as rng

BACKGROUND = "#b1ddc6"
ENCODING = "utf-8"


def removeCard():
	global data_dict, index
	data_dict.pop(index)
	dataFrame = pd.DataFrame(data_dict)
	dataFrame.to_csv("./data/words_to_learn.csv", index=False, encoding=ENCODING)
	createCard()


def createCard():
	global data_dict, index, flip

	window.after_cancel(flip)
	index = rng.randint(0, len(data_dict) - 1)
	word = data_dict[index]["French"]
	canvas.itemconfig(canvasImg, image=pic_front)
	canvas.itemconfig(canvasLang, text="French", fill="black")
	canvas.itemconfig(canvasWord, text=word, fill="black")
	flip = window.after(3000, flipCard)


def flipCard():
	global data_dict, index

	word = data_dict[index]["English"]
	canvas.itemconfig(canvasImg, image=pic_back)
	canvas.itemconfig(canvasLang, text="English", fill="white")
	canvas.itemconfig(canvasWord, text=word, fill="white")


try:
	file = open("./data/words_to_learn.csv", "r", encoding=ENCODING)
except FileNotFoundError:
	file = open("./data/french_words.csv", "r", encoding=ENCODING)
finally:
	data = pd.read_csv(file)
	data_dict = data.to_dict(orient="records")

index = 0
window = tk.Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND)

pic_front = tk.PhotoImage(file="./images/card_front.png")
pic_back = tk.PhotoImage(file="./images/card_back.png")
succes = tk.PhotoImage(file="./images/right.png")
fail = tk.PhotoImage(file="./images/wrong.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
canvasImg = canvas.create_image(400, 263, image=pic_front)
canvasWord = canvas.create_text(400, 263, text="Word", fill="black", font=("arial", 60, "bold"))
canvasLang = canvas.create_text(400, 150, text="Language", fill="black", font=("arial", 40, "italic"))
canvas.config(bg=BACKGROUND)
canvas.grid(column=0, row=0, columnspan=2)

button_check = tk.Button(image=succes, bg=BACKGROUND, pady=0, padx=0, border=0,
						 highlightthickness=0, highlightbackground=BACKGROUND, highlightcolor=BACKGROUND)
button_check.config(command=removeCard)
button_check.grid(column=1, row=1)

button_cross = tk.Button(image=fail, bg=BACKGROUND, pady=0, padx=0, border=0,
						 highlightthickness=0, highlightbackground=BACKGROUND, highlightcolor=BACKGROUND)
button_cross.config(command=createCard)
button_cross.grid(column=0, row=1)

flip = window.after(3000, createCard)

window.mainloop()
