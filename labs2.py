import random
from tkinter import *

list_size = 500

def click(event):
    global round
    print(event.x, event.y)
    round.append(Round(canvas, event.x , event.y , event.x, event.y))
    canvas.configure(bg='black')

class Round:
    def __init__(self, canvas, x_o=300 , y_o=580, x=300, y=580):
        self.oval = canvas.create_oval(x_o, y_o, x + 20, y + 20, width=3, fill='blue', stipple="gray50")
        self.brightness = 1
        self.live = random.randint(100, 300)
        self.canvas = canvas
        self.x = 0
        self.y = 0

    def destroy(self):
        self.canvas.delete(self.oval)

    def move(self):
        # delta = random.randint(1, 100)
        self.x += float(random.uniform(0, 0.4) - random.uniform(0, 0.4))
        self.y -= 0.05
        self.canvas.move(self.oval, self.x, self.y)
        self.live -= 1
        if self.live <= 0:
            self.destroy()
            return False
        return True

root = Tk()
root['bg'] = '#fafafa'
root.title('Анимация')
win_size = 600
canvas = Canvas(root, width=win_size, height=win_size, bg="black")

canvas.pack()
x_oval = win_size / 2
y_oval = win_size - 20
round = [Round(canvas) for i in range(list_size)]
oval = canvas.create_oval(x_oval, y_oval, x_oval + 20, y_oval + 20, width=3, fill='blue', stipple="gray50")
root.bind('<Button-1>', click)


def motion():
    global round
    for r in round:
        if not r.move():
            round.remove(r)
            if(len(round) == list_size - 1):
                round.append(Round(canvas))
    root.after(3, motion)


motion()
root.mainloop()