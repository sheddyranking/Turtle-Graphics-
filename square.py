import turtle

square = turtle.Turtle()

#add color, you could use hash codes, 
#the first color cloud the area, and the second color draws a margin around.
square.color("blue", "cyan")

#wrap your design in begin.fill() and end.fill() ,function to cloud the color
#you cound wrap each square  with begin() and end() fill or wrap them in one begin() and end() fill
square.begin_fill()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
#square.end_fill()

#the penup() and pendown() function will  help break out of the first square.
square.penup()
square.forward(100)
square.pendown()

#square.begin_fill()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.end_fill()







turtle.done()