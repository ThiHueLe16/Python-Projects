from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#65B741"
FONT = ("Times new romand", 20, "bold ")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score:0/0", font=FONT, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="#C1F2B0", highlightthickness=0)
        self.quiz = quiz
        self.canvasText = self.canvas.create_text(150, 125, width=280, text="Some question", fill="orange",
                                                  font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=50)
        rightPhoto = PhotoImage(file="images/true.png")
        self.rightButton = Button(image=rightPhoto, highlightthickness=0,command= self.truePressed)
        self.rightButton.grid(row=2, column=1)
        wrongPhoto = PhotoImage(file="images/false.png")
        self.wrongButton = Button(image=wrongPhoto, highlightthickness=0, command=self.falsePressed)
        self.wrongButton.grid(row=2, column=0)

        self.getNextQuestion()
        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.config(bg="#C1F2B0")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvasText, text=question, fill="#65B741")
        else:
            self.canvas.itemconfig(self.canvasText, text="You have reach the end of the question list",fill="#65B741")
            self.rightButton.config(state="disabled")
            self.wrongButton.config(state="disabled")

    def truePressed(self):
        self.getFeedback(self.quiz.check_answer("True"))

    def falsePressed(self):
        self.getFeedback(self.quiz.check_answer("False"))

    def getFeedback(self, isRight):

        if isRight:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvasText, text="You got it right!", fill="white")
        else:
            self.canvas.itemconfig(self.canvasText, text="That's wrong.",fill="white")
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")

        self.window.after(1000, self.getNextQuestion)