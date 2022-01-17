import turtle

square = turtle.Turtle()

#add color, you could use hash codes, 
#the first color cloud the area, and the second color draws a margin around.
square.color("blue", "cyan")

#wrap your design in begin.fill() and end.fill() ,function to cloud the color
square.begin_fill()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.end_fill()








turtle.done()