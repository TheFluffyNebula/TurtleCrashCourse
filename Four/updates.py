import time
import turtle

# draw fast
turtle.speed(0)

# tracer(0) --> only update when update is called
turtle.tracer(0)

for i in range(10):
    turtle.up()
    turtle.goto(i * 10, i * 10)
    turtle.down()
    for j in range(4):
        turtle.fd(5)
        turtle.left(90)
time.sleep(2)
turtle.update()

for i in range(10):
    turtle.up()
    turtle.goto(-i * 10, -i * 10)
    turtle.down()
    for j in range(4):
        turtle.fd(5)
        turtle.left(90)
time.sleep(2)
turtle.update()

turtle.done()
