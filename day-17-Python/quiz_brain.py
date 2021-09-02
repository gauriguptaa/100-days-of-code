class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        users_input = input(
            f"Q{self.question_number}: {self.question_list[self.question_number - 1].question}. (True/False)")
        correct_answer = self.question_list[self.question_number - 1].correct_answer
        self.check_answer(users_input, correct_answer)

    def check_answer(self, user_input, answer):
        if user_input == answer:
            self.score += 1
            print(f"You got it correct.\nYour score is: {self.score}/{self.question_number}")
        else:
            print(f"Sorry Incorrect answer.\nYour score is: {self.score}/{self.question_number}")
        print()

