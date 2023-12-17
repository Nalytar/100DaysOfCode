from tkinter import *
import time
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

	def __init__(self, QuizBrain):
		self.quiz = QuizBrain
		self.falseImage = PhotoImage
		self.trueImage = PhotoImage
		self.canvas = Canvas
		self.canvasText = None
		self.label = Label
		self.falseButton = Button
		self.trueButton = Button

		self.window = Tk()
		self.window.title("Quiz-Game")
		self.window.config(bg=THEME_COLOR, padx=20, pady=20)

		self.createScoreCounter()
		self.createQuestionCanvas()
		self.createTrueButton()
		self.createFalseButton()
		self.getNextQuestion()

		self.window.mainloop()

	def createScoreCounter(self):
		self.label = Label(text="Score: 0", bg=THEME_COLOR, font=("arial", 16, "normal"), fg="white", justify="center")
		self.label.grid(column=1, row=0)

	def createQuestionCanvas(self):
		self.canvas = Canvas(width=300, height=250, bg="white")
		self.canvasText = self.canvas.create_text(150, 125, font=("arial", 20, "italic"), width=280)
		self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

	def createTrueButton(self):
		self.trueImage = PhotoImage(file="./images/true.png")
		self.trueButton = Button(image=self.trueImage, highlightthickness=0, command=self.check_answer_true)

		self.trueButton.grid(column=0, row=2)

	def createFalseButton(self):
		self.falseImage = PhotoImage(file="./images/false.png")
		self.falseButton = Button(image=self.falseImage, highlightthickness=0, command=self.check_answer_false)

		self.falseButton.grid(column=1, row=2)

	def getNextQuestion(self):
		q_text = self.quiz.next_question()
		self.canvas.itemconfig(self.canvasText, text=q_text)

	def check_answer_true(self):
		self.giveFeedback(self.quiz.check_answer("True"))

	def check_answer_false(self):
		self.giveFeedback(self.quiz.check_answer("False"))

	def giveFeedback(self, isRight):
		if isRight:
			self.canvas.config(background="green")
		else:
			self.canvas.config(background="red")

		self.window.after(1000, self.resetCanvas)

	def resetCanvas(self):
		if self.quiz.still_has_questions():
			self.canvas.config(background="white")
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.canvasText, text=q_text)
			self.label.config(text=f"Score: {self.quiz.score}")
		else:
			self.trueButton.config(state="disabled")
			self.falseButton.config(state="disabled")

			self.canvas.config(bg="white")
			self.canvas.itemconfig(self.canvasText,
			                       text=F"There is no Question\nYour Score: {self.quiz.score}/{self.quiz.question_number}")
