# print("Hello World!")
import turtle
screen = turtle.Screen()
# make the initial window 800x800
screen.setup(800, 800)
# turtle.speed(0)
'''
turtle.left(x) turns turtle left by x degrees
turtle.right(x) turns turtle right by x degrees
turtle.seth(x) turns turtle to x degrees (think pre-calc unit circle)
'''

# we can also get the turtle to move forward in the direction it's facing
for i in range(4):
    turtle.fd(100)
    turtle.left(90)

# we can pick up the pen to not draw
turtle.up()
turtle.goto(-200, -200)
# put the pen down to draw again
turtle.down()
for i in range(4):
    turtle.fd(100)
    turtle.right(90)

turtle.up()
turtle.goto(200, -200)
turtle.down()
for i in range(4):
    turtle.fd(100)
    turtle.seth((i + 1) * 90)

turtle.done()
