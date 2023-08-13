class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def finished(self):
        return self.question_number == 4

    def next_question(self, random_index):
        self.question_number += 1
        current_question = self.questions_list[random_index]
        prompt = f"Q {self.question_number}: {current_question.text} (True/False)?: "
        guess = input(prompt).title()
        if (guess != "True") and (guess != "False"):
            correct = False
            while not correct:
                print("Please type valid option.")
                guess = input(prompt).title()
                if (guess == "True") or (guess == "False"):
                    correct = True
        if guess == current_question.answer:
            self.score += 1
            print(f"Correct! The answer: {current_question.answer}")
        elif guess != current_question.answer:
            print(f"The answer was {current_question.answer}. Better luck next time!")
        print(f"Score: {self.score}/4")
        self.questions_list.remove(current_question)
