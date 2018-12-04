from turtle import Turtle

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.color(orange)

def circle(Length, angle):
    for time in range(4):
        my_turtle.forward(Length)
        my_turtle.left(angle)

for time in range(100)  :
    circle(200, 120)
    my_turtle.left(11)
