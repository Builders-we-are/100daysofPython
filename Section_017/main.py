from os import system

system("clear")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index, question in enumerate(question_data):
    # new_q = Question(question_data[i]["text"], question_data[i]["answer"])
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(len(question_bank))
print(question_bank[0].text)


quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
