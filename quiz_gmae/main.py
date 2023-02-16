from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for item in question_data:
    question_text=item["text"]
    question_answer=item["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
FLAG=True

while quiz.still_has_question():
    quiz.next_question()
