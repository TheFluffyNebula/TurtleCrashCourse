import turtle

# output will be in terminal
turtle.up()
turtle.hideturtle()
turtle.goto(200, 200)
tx = turtle.xcor()
ty = turtle.ycor()
turtle.goto(400, 400)
print(f"Turtle original location: ({tx}, {ty})")

# turtle.done()
