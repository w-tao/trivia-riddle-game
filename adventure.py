from tkinter import Tk, Canvas, PhotoImage, Label, Button

#functions
def riddle_game():
    import riddle

def trivia_game():
    import trivia

#Defining widgets
main = Tk()

title = Label (main, text = "HAPPY", font = "Verdana 30 bold", )

instructions = Label(main, text = "There is a happy face, he's just happy to see you. You hate him and want to get out of here. What do you do?")

trivia = Button(main, text = "Play trivia game", command = trivia_game)

riddle = Button(main, text = "Play riddle game", command = riddle_game)

filename = PhotoImage(file = 'project_pictures/' + 'menuPic.gif')

background_label = Label(main, image=filename)

#Setting up screen
main.geometry("900x600") 
title.pack()
instructions.pack()
background_label.pack()
trivia.pack()
riddle.pack()

#Begin mainloop 
main.mainloop()
