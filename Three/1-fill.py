import turtle

turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(100, 0)
turtle.goto(50, 50)
turtle.goto(0, 0)
turtle.end_fill()

turtle.up()
turtle.goto(-100, -100)
turtle.down()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(-300, -300)
turtle.goto(-100, -300)
turtle.goto(-100, -100)
turtle.end_fill()

turtle.done()
