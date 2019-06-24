import sys
from tkinter import Tk, PhotoImage, Label, Button
from random import randint, choice

def update_time():
    if state:
        global tick
        tick += 1
        time['text'] = tick
        
        click = Label(root, text = "QUICK! Click the picture!", fg = "orchid", font=("HanziPen TC", 20))
        click.pack()
        click.place(x = 340, y = 110)

    time.after(100, update_time)

def start():
    global state
    state = True
    
def stop():
    global state
    state = False
    picture.pack_forget()

points = 0
points = points - 60
root = Tk()
root.geometry("900x600")

tick = 0
state = True
time = Label(root, fg='orchid', font=("HanziPen TC", 90))
time.pack() 

img_file = choice(["deer.gif", "dog.gif", "doggie.gif", "doggiebasketball.gif", "kitty.gif"])
photo = PhotoImage(file = 'project_pictures/' + img_file)
picture = Button(root, image = photo, command = stop)
picture.pack()
picture.place(x = randint(200, 500), y = randint(200, 500))

button_photo = PhotoImage(file = 'project_pictures/' + 'pink(1).gif')
button_back = Label(root, image = button_photo)
button_setting = Button(root, text = "Click here to quit!", fg = "Black", font=("HanziPen TC", 15), command = quit)
button_setting.pack()
button_back.pack()
button_back.place(x = 20, y = 30)
button_setting.place(x = 40, y = 40)

update_time()
root.mainloop()
