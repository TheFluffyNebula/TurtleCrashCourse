import turtle

screen = turtle.Screen()

def move_forward():
    turtle.forward(50)

def turn_left():
    turtle.left(90)

def turn_right():
    turtle.right(90)

screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()
turtle.done()
