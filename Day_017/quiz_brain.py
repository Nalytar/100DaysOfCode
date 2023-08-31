class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False) ")
        self.check_answer(answer)

    def still_has_question(self):
        while self.question_number < len(self.question_list):
            self.next_question()
            self.question_number += 1
            print("\n----------------------------------------------\n")
        print("You've completed the quiz!")
        print(f"Your Final Score was: {self.score}/{self.question_number}")

    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
