from Datas import data
from quiz import Quizaction

question_bank = []

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

for question in data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = Quizaction(question_bank)

while quiz.questions():
    quiz.next_question()

print("You've completed the quiz.py")
print(f"Your final score was: {quiz.score}/{quiz.q_num}🎉")
