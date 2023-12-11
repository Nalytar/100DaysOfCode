# udemy Course - 100 Days of Code - Python
# 1XX: Hold on
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You screwed up
# 5XX: I screwed up

import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.raise_for_status())

from tkinter import *


def get_quote():
	response = requests.get(url="https://api.kanye.rest")
	responseJson = response.json()
	canvas.itemconfig(quote_text, text=responseJson["quote"])

# Write your code here.


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
								fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
