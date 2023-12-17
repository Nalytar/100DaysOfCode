import html

import requests

data = requests.get("https://opentdb.com/api.php?amount=15&category=15&type=boolean")
data.raise_for_status()

dataJson = data.json()

question_data = []

for dicData in dataJson["results"]:
    questionData = {"category": dicData["category"],
                    "type": dicData["type"],
                    "difficulty": dicData["difficulty"],
                    "question": html.unescape(dicData["question"]),
                    "correct_answer": dicData["correct_answer"],
                    "incorrect_answers": dicData["incorrect_answers"]}

    question_data.append(questionData)
