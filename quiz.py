import tkinter as tk 
from time import sleep
from tkinter import Tk, PhotoImage, Label, Button
from random import randint, choice
import sys
root = tk.Tk()
root.geometry("900x600")

photo = PhotoImage(file = 'project_pictures/' + 'penguin.gif')
picture = Label(root, image = photo)
picture.pack()
picture.place(x = -25, y = 150)

'''class React:
    def __init__(self, root, points):
        self.tick = 0
        self.points = points
        self.state = True
        self.root = root
        self.frame = Frame(root)
        self.frame.pack(side = 'top')
        self.frame.grid(row = 1, column = 1)
        self.time = Label(self.frame, fg='orchid', font=("HanziPen TC", 90))
        self.time.pack()

        img_file = choice(["deer.gif", "dog.gif", "doggie.gif", "doggiebasketball.gif", "kitty.gif"])
        photo = PhotoImage(file = 'project_pictures/' + img_file)
        self.picture = Button(self.frame, image = photo, command = stop)
        self.picture.pack()
        self.picture.place(x = randint(200, 500), y = randint(200, 500))

        button_photo = PhotoImage(file = 'project_pictures/' + 'pink(1).gif')
        button_back = Button(self.frame, image = button_photo)
        button_setting = Button(self.frame, text = "Click here to quit!", fg = "Black", font=("HanziPen TC", 15), command = quit)
        button_setting.pack()
        button_back.pack()
        button_back.place(x = 20, y = 30)
        button_setting.place(x = 30, y = 40)

    def update_time(self):
        if self.state:
            self.tick += 1
            self.time['text'] = tick 
            
            click = Label(self.frame, text = "QUICK! Click the picture!", fg = "orchid", font=("HanziPen TC", 20))
            click.pack()
            click.place(x = 340, y = 110)

        self.time.after(100, update_time)
    
    def start(self):
        self.state = True
        
    def stop(self):
        self.state = False

    reaction = React(root, 0)
    reaction.update_time()
    root.mainloop()'''

class Question:
    def __init__(self, question, answers, correct_letter):
        self.question = question
        self.answers = answers
        self.correct_letter = correct_letter

    def check(self, letter, view):
        global right
        if(letter == self.correct_letter):
            label = tk.Label(view, text="Correct!")
            right += 1
        else:
            label = tk.Label(view, text="Incorrect!")

        label.pack()
        view.after(1000, lambda *args: self.unpack_view(view))

    def get_view(self, root):
        view = tk.Frame(root)
        label = tk.Label(view, text=self.question)
        label.pack()
        button_a = tk.Button(view, text=self.answers[0], command=lambda *args: self.check("A", view))
        button_a.pack()
        button_b = tk.Button(view, text=self.answers[1], command=lambda *args: self.check("B", view))
        button_b.pack()
        button_c = tk.Button(view, text=self.answers[2], command=lambda *args: self.check("C", view))
        button_c.pack()
        button_d = tk.Button(view, text=self.answers[3], command=lambda *args: self.check("D", view))
        button_d.pack()
        return view

    def unpack_view(self, view):
        view.pack_forget()
        ask_question()

def ask_question():
    global questions, root, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        tk.Label(root, text="You got " + str(right) + " out of " + str(number_of_questions) + " questions answered correctly!").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].get_view(root).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    question_string = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correct_letter = file.readline()
    correct_letter = correct_letter[:-1]
    questions.append(Question(question_string, answers, correct_letter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

button = tk.Button(root, text="Start", command=ask_question)
button.pack()
root.mainloop()