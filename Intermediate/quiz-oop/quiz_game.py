from data import question_data
from question_model import Question
from brain_class import Brain

question_bank=[]
for question in question_data:
    new_question = Question(text=question["question"],answer=question["correct_answer"])
    question_bank.append(new_question)


quiz = Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")