class Quizaction:

    def __init__(self, qlist):
        self.q_num = 0
        self.score = 0
        self.qlist = qlist

    def questions(self):
        return self.q_num < len(self.qlist)

    def next_question(self):
        current_question = self.qlist[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}:{current_question.text}\n(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You found correct answer👌!")
        else:
            print("Wrong answer!!")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")
