from tkinter import *
from quiz_brain import *

from tkmacosx import Button
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(padx= 20, pady = 20, bg = THEME_COLOR)

        self.scoreLb = Label(text = "Score: ", fg= "white", bg= THEME_COLOR)
        self.scoreLb.grid(column = 1, row= 0)

        self.canvas = Canvas(height= 250, width= 300, bg= "white")

        self.question_text = self.canvas.create_text(150, 120,
                                                     text= "Place for question",
                                                     fill = "black",
                                                     font = "Arial 20 italic",
                                                     width= 280)

        self.canvas.grid(column = 0, row = 1, columnspan= 2, pady= 20)



        wrongImg = PhotoImage(file = "images/false.png")

        self.wrongBtn = Button(image = wrongImg,
                               bg = THEME_COLOR,
                               fg = THEME_COLOR,
                               borderwidth = 4,
                               activebackground = (THEME_COLOR, THEME_COLOR),
                               activeforeground= "white",
                               command= self.wrongButtonPressed

                               )

        self.wrongBtn.grid(column = 0, row = 2)


        # right button


        rightImg = PhotoImage(file = "images/true.png")
        self.rightBtn = Button(image = rightImg,
                              bg = THEME_COLOR,
                              fg = THEME_COLOR,
                              borderwidth = 4,
                              activebackground = (THEME_COLOR, THEME_COLOR),
                              activeforeground= THEME_COLOR,
                              command= self.rightButtonPressed

                          )

        self.rightBtn.grid(column = 1, row= 2)

        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.config(bg= "white")
        if self.quiz.still_has_questions():
            self.scoreLb.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "you have reached the end of this quiz")
            self.wrongBtn.config(state= "disabled")
            self.rightBtn.config(state= "disabled")


    def wrongButtonPressed(self):

        self.give_feedback(self.quiz.check_answer("False"))
    def rightButtonPressed(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, feedback: bool):
        if feedback is True:
            self.canvas.config(bg = "light green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.getNextQuestion)
        
