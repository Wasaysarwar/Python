import turtle
# import time

animation = turtle.Turtle()
animation.speed(40)
animation.hideturtle()
animation.getscreen().bgcolor("black")
animation.color("aqua")

for i in range(170):
    animation.circle(i)
    animation._rotate(5)
    
# time.sleep(2)
   