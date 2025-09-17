# print("Hello World!")
import turtle
screen = turtle.Screen()
# make the initial window 800x800
screen.setup(800, 800)

# turtle starts at (0, 0)
# moving the turtle while it's down produces lines!
turtle.goto(100, 100)
turtle.goto(200, 0)
turtle.goto(300, 100)
turtle.goto(400, 0)

# prevent automatically exiting (equivalent to turtle.done())
screen.mainloop()
