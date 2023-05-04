from random import *
from tkinter import *
size = 1000
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()
while True:
    col = choice(['pink', 'orange', 'purple', 'yellow', 'green', 'blue', 'brown', 'black', 'maroon'])
    # x value
    x0 = randint(0, size)
    # y value
    y0 = randint(0, size)
    d = randint(0,size/5)
    canvas.create_oval(x0, y0,x0 + d, y0 + d, fill=col)
    window.update()
