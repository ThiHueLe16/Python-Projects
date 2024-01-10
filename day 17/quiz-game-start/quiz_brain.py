class Quizbrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {question_text}. (True/False)?')
        self.check_answer(answer, question_answer)


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print("you got it right!")
        else:
            print("That's wrong.")
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print()