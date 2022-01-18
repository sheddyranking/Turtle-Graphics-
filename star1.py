import turtle

star = turtle.Turtle()
star.getscreen().bgcolor("#994444") #changes background color 
star.speed(20) #speed up the drawing 


star.penup()
star.goto((-200, 100))
star.pendown()

#the functions that draws the star shape
def sheddy(draw, size):
    if size <= 10: # the recursive statement
        return
    else:
        star.begin_fill()
        for i in range(5):
            draw.forward(size)
            sheddy(draw, size/3)
            draw.left(216)
        star.end_fill()

sheddy(star, 360) #pass in the const variable and the value of the size 




turtle.done()