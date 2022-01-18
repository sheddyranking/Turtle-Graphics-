import turtle

flower = turtle.Turtle()
flower.color("red", "yellow") #red for the edge and yellow for the fill.
flower.speed(10) #speed up thee drawing 


flower.begin_fill()
for i in range(100): # the statement that draws the flower shape
    flower.forward(300)
    flower.left(170)


flower.end_fill()



turtle.done()