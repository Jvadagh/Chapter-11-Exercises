"""
18. Modify Listing 9.14 (tkinterlight.py) so that it models a light with a single on/off yellow lamp.
"""

from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame


def DoOnOff():
    global color
    if color == 'yellow':
        color = 'black'
        canvas.itemconfigure(yellow_lamp, fill='black')

    elif color == 'black':
        color = 'yellow'
        canvas.itemconfigure(yellow_lamp, fill='yellow')


color = 'yellow'
root = Tk()
root.title("yellow light")
frame = Frame(root)
frame.pack()
canvas = Canvas(frame, width=300, height=300)
canvas.create_rectangle(50, 20, 150, 280, fill='gray')
yellow_lamp = canvas.create_oval(70, 120, 130, 180, fill='yellow')
button = Button(frame, text='ON/OFF', command=DoOnOff)
button.grid(row=0, column=0)
canvas.grid(row=0, column=1)
root.mainloop()
