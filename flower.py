import turtle

flower = turtle.Turtle()
flower.color("red", "yellow")
flower.speed(10)


flower.begin_fill()
for i in range(100):
    flower.forward(300)
    flower.left(170)


flower.end_fill()



turtle.done()