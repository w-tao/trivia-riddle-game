import sys
from tkinter import Tk, PhotoImage, Label, Button
screen = Tk()
screen.geometry("1000x600")

points = 100

photos = PhotoImage(file = 'project_pictures/' + "deers.gif")
background = Label(screen, image = photos)
background.pack()
background.place(x = -50, y = 190)

photo2 = PhotoImage(file = 'project_pictures/' + "foxie.gif")
background2 = Label(screen, image = photo2)
background2.pack()
background2.place(x = 180, y = 0)

photo3 = PhotoImage(file = 'project_pictures/' + "owl.gif")
background3 = Label(screen, image = photo3)
background3.pack()
background3.place(x = 650, y = -50)

photo4 = PhotoImage(file = 'project_pictures/' + "penguin.gif")
background4 = Label(screen, image = photo4)
background4.pack()
background4.place(x = 350, y = 350)

end_game = Label(screen, text = "GAME OVER", fg = "orchid", font=("HanziPen TC", 85))
end_game.pack()
end_game.place(x = 200, y = 170)

point_teller = Label(screen, text = "Total number of points: " + str(points) + "!", fg = "orchid", font=("HanziPen TC", 30))
point_teller.pack()
point_teller.place(x = 300, y = 300)

button_photo = PhotoImage(file = 'project_pictures/' + 'pink.gif')
button_back = Label(screen, image = button_photo)
button_setting = Button(screen, text = "Click here to quit!", fg = "Black", font=("HanziPen TC", 15), command = quit)
button_setting.pack()
button_back.pack()
button_back.place(x = 20, y = 30)
button_setting.place(x = 38, y = 42)

screen.mainloop()
