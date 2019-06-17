from tkinter import Tk, Canvas, PhotoImage, Label, Button 

#functions
def button_clicked(name, text):
    print(text)
    name.pack_forget()

#Defining widgets
main = Tk()

title = Label (main, text = "HAPPY", font = "Verdana 30 bold", )

instructions = Label(main, text = "There is a happy face, he's just happy to see you. You hate him and want to get out of here. What do you do?")

flee = Button( main, text = "Flee from him", command = button_clicked(flee, "You fled") )

go_through_wall = Button( main, text = "Go into the floor", command = button_clicked(go_through_wall, "You went through the wall"))

fly = Button( main, text = "Fly away", command = button_clicked(fly, "You flew away"))

filename = PhotoImage(file = "C:\\Users\\localaccount\\Pictures\\happy.gif")

background_label = Label(main, image=filename)

#Setting up screen
main.geometry("900x600") 
title.pack()
instructions.pack()
background_label.pack()
flee.pack()
crawl.pack()
fly.pack()

#Begin mainloop 
main.mainloop()
