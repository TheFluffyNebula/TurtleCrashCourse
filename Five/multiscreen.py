from turtle import RawTurtle, TurtleScreen
from tkinter import *

class Window(Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.running = True
        self.geometry(geometry)
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.destroy_window)
        self.canvas = Canvas(self)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.turtle = RawTurtle(TurtleScreen(self.canvas))

    def update_window(self):
        if self.running:
            self.update()

    def destroy_window(self):
        self.running = False
        self.destroy()

# create windows
win1 = Window('Turtle Window 1', '640x480+0+0')
win2 = Window('Turtle Window 2', '640x480+650+0')

# assign turtles
t1 = win1.turtle
t2 = win2.turtle

# draw stuff
t1.pendown()
t1.forward(100)
t2.pendown()
t2.backward(100)

# update windows (the mainloop)
while win1.running or win2.running:
    win1.update_window()
    win2.update_window()
