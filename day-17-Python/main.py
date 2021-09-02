from question_model import Question
from data import movies
from quiz_brain import QuizBrain
if __name__ == '__main__':
    question_bank = []
    for question in movies:
        question_obj = Question(question["question"], question["correct_answer"])
        question_bank.append(question_obj)
    quizBrain = QuizBrain(question_bank)
    while quizBrain.still_has_questions():
        quizBrain.next_question()
    print("You've reached the end of the Quiz.")
    print(f"Your Final Score is: {quizBrain.score} / {quizBrain.question_number}")

