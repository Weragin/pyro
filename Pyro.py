import tkinter as tk
import random as rnd

win = tk.Tk()
win.title('Pyrotechnic simulator')

label = tk.Label(text='Pyrotechnic', fg='red', font='Arial 22')
label.pack()

label = tk.Label(text='Choose the correct cable or else you die!!!')
label.pack()

canvas = tk.Canvas(win, height=500, width=500, bg='#a0a0a0')
canvas.pack()

difficulty = 5
COLOURS = ('white', 'black', 'magenta', 'pink', 'blue', 'green', 'yellow', 'orange', 'grey', 'red')
SIZEX = 123
SIZEY = 10

for i in range(difficulty):
    canvas.create_rectangle((30, 10 + (SIZEY + 1) * i, 30 + SIZEX, 10 + (SIZEY + 1) * i + SIZEY),
                            fill=rnd.choice(COLOURS), )


def on_click(e):
    overlap = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)


canvas.bind('<1>', on_click)
tk.mainloop()
