from tkinter import *

BLACK = "#000000"
THEME_COLOR = "#375362"
WHITE = "#ffffff"
RED = "#ee6868" 
GREEN = "#77f573" 

class QuizInterface:
    
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.question = self.quiz.next_question()

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        #--------------------Question Canvas--------------------#
        self.canvas = Canvas(height=250, width=300, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 125, text=self.question, width=250, font=("Arial", 20, "italic"), fill = BLACK)
        self.canvas.grid(pady=50, column=0, row=1, columnspan=2)

        #--------------------Score Text--------------------#
        self.score_text = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg=WHITE ,font=("Arial", 15))
        self.score_text.grid(column=1, row=0, sticky="e")
        
        #--------------------Buttons--------------------#
        check_image = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=check_image, highlightthickness=0, command=self.check_click)
        self.correct_button.grid(pady=20, column=0, row=2)

        cross_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=cross_image, highlightthickness=0, command=self.cross_click)
        self.wrong_button.grid(pady=20, column=1, row=2)

        self.window.mainloop()

    def reset_canvas(self):
        self.canvas.config(bg=WHITE)

    def get_answer(self):
        self.reset_canvas()
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def give_feedback(self, is_right):
        self.score_text.config(text=f"Score: {self.quiz.score}")

        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, self.get_answer)
        

    def check_click(self):
        self.give_feedback(self.quiz.check_answer("True"))
        

    def cross_click(self):
        self.give_feedback(self.quiz.check_answer("False"))