# udemy Course - 100 Days of Code - Python
# GUI - https://docs.python.org/3/library/tk.html
import tkinter as tk


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CORAL = "#ff7f50"
FONT_NAME = "Courier"
WORK_TIME = 25
SHOT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# TIMER RESET
def reset_Timer():
	global reps
	global timer

	window.after_cancel(timer)
	reps = 0
	action.config(text="")
	label.config(text="Timer", fg=GREEN)
	canvas.itemconfig(timer_label, text="00:00")


# TIMER MECHANISM
def start_Timer():
	global reps
	if reps == 8:
		reps = 0

	reps += 1

	if reps % 2 != 0:
		# Long Time
		label.config(text="Work", fg=GREEN)
		countdown(WORK_TIME * 60)
	elif reps % 8 == 0:
		# Long Break
		label.config(text="Break", fg=RED)
		countdown(LONG_BREAK_MIN * 60)
	else:
		# Short Break
		label.config(text="Break", fg=PINK)
		countdown(SHOT_BREAK_MIN * 60)


# COUNTDOOWN MECHANISM
def countdown(count):
	global reps
	global timer

	displayedTime = (str(count // 60) + ":" + f"{count % 60:02d}")
	canvas.itemconfig(timer_label, text=displayedTime)

	if count >= 0:
		timer = window.after(1000, countdown, count - 1)
	else:
		start_Timer()
		number = round(reps // 2)
		marks = ""
		for n in range(0, number):
			marks += "✔"
		action.config(text=marks)


# UI SETUP
window = tk.Tk()
window.title("Pomodore Work Timer")
window.config(background=YELLOW, padx=100, pady=50)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = tk.Label(text="Timer")
label.config(font=(FONT_NAME, 35, "bold"), fg=GREEN, background=YELLOW)
label.grid(column=1, row=0)

action = tk.Label()
action.config(fg=GREEN, background=YELLOW, font=(FONT_NAME, 25, "bold"))
action.grid(column=1, row=3)

start_btn = tk.Button(text="Start")
start_btn.config(background=CORAL, command=start_Timer)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(text="Reset")
reset_btn.config(background=CORAL, command=reset_Timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
