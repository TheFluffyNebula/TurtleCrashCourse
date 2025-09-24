fill
* turtle.fillcolor(name)
* turtle.begin_fill()
* **draw the shape**
* turtle.end_fill()

hiding the turtle, tracking coordinates
* turtle.hideturtle() or turtle.ht()
* turtle.showturtle()
* storedX = turtle.xcor()
* storedY = turtle.ycor()

writing text
* default params: 
    * turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
    * arg: object to be written to the TurtleScreen
        * often a string
    * move: if True, moves the pen to the bottom right of text
    * align: 'left', 'center', or 'right'
    * font: (fontname, fontsize, fonttype)

next up:
* animation (instant update)
