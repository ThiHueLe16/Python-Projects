from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz=Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    still_has_question= quiz.still_has_question()
print(".................................................................................................")
print(".................................................................................................")
print("You have completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")
