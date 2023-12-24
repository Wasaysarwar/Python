import turtle

animation = turtle.Turtle()
animation.speed(40)
animation.hideturtle()
animation.getscreen().bgcolor("black")
animation.color("aqua")

for i in range(170):
    animation.circle(i)
    animation.rotate(5)