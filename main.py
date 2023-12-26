from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import secrets

question_bank = []

for i in question_data:
    q_text = i["text"]
    q_answer = i["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

rand_index = secrets.SystemRandom().randint(0, len(question_bank) - 1)
quiz = QuizBrain(question_bank)
print("\n")

while not quiz.finished():
    quiz.next_question(rand_index)
    rand_index = secrets.SystemRandom().randint(0, len(question_bank) - 1)

print(f"\nYour final score: {quiz.score}/{quiz.question_number}")
