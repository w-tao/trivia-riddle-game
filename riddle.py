import tkinter as tk 
from sys import argv
import time
class Riddle_Game:
    def __init__(self, question, answers, correct_choice):
        self.question = question
        self.answers = answers
        self.correct_choice = correct_choice

    def check(self, var, view):
        global right
        choice = var.get()
        if(choice == self.correct_choice):
            label = tk.Label(view, text="Correct ツ", fg = 'forestgreen')
            right += 1
            
        else:
            label = tk.Label(view, text="yOuR wRoNg >:", fg = 'red')
            go_to_reaction()
            
        label.pack(side='top')
        
        view.after(1000, lambda *args: self.unpack_view(view))

    def get_view(self, root):
        view = tk.Frame(root, borderwidth=5, relief=tk.RAISED, padx=20, pady=5)
        label = tk.Label(view, text=self.question)
        label.pack(side='top')
        var = tk.IntVar()
        
        button_a = tk.Radiobutton(view, text=self.answers[0], variable=var, value=1, command=lambda *args: self.check(var, view))
        button_a.pack(anchor='w')
        
        button_b = tk.Radiobutton(view, text=self.answers[1], variable=var, value=2, command=lambda *args: self.check(var, view))
        button_b.pack(anchor='w')
        
        button_c = tk.Radiobutton(view, text=self.answers[2], variable=var, value=3, command=lambda *args: self.check(var, view))
        button_c.pack(anchor='w')
        
        button_d = tk.Radiobutton(view, text=self.answers[3], variable=var, value=4, command=lambda *args: self.check(var, view))
        button_d.pack(anchor='w')

        timer_font = ('Wawati SC', 69, "italic")		
        self.clock = tk.Label(view, text="", width=10, pady=100, font=timer_font, fg = 'orange')		
        self.clock.pack(side='bottom')		
        self.remaining = 0		
        self.countdown(30)		

        return view

    def unpack_view(self, view):
        view.pack_forget()
        ask_question()

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.clock.configure(text="Time's Up!")
        else:
            self.clock.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.clock.after(1000, self.countdown)

def go_to_reaction():
    import game.py

def ask_question():
    global questions, root, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        tk.Label(root, text="You got " + str(right) + " out of " + str(number_of_questions) + " questions answered correctly. " + str(right)*2 + " Points! Fantastic!").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].get_view(root).pack(side='top')
    
### Main Script
# Read from the text file
with open('questions.txt', "r") as quiz_file:
    questions = []
    line = quiz_file.readline().rstrip()
    while(line != ""):
        question_string = line # Question
        answers = []
        for i in range(4):
            answers.append(quiz_file.readline().rstrip()) # Four answer choices

        correct_choice = quiz_file.readline().rstrip() # Correct choice
        questions.append(Riddle_Game(question_string, answers, int(correct_choice)))
        line = quiz_file.readline().rstrip() # Potential next question

index = -1
right = 0
number_of_questions = len(questions)

# Check the content loading
root = tk.Tk()
root.geometry('1200x500')
root.title("Adventure Trivia Riddle Reaction Game")
button = tk.Button(root, text="Begin", command=ask_question)
#button.pack(side='top')
button.pack(anchor='n')
root.mainloop()

'''
background_image = tk.PhotoImage('detective_background.gif')
background_label = tk.Label(root, image=background_image)
background_label.pack()
'''