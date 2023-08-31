from Day_017.quiz_brain import *
from quiz_game_data import *
from question_model import *

questing_bank = []

for question in question_data:
    questing_bank.append(Question(question["question"], question["correct_answer"]))

question_brain = QuizBrain(questing_bank)
question_brain.still_has_question()


