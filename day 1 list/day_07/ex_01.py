import turtle
import random
import time

screen=turtle.Screen()
screen.title('DATAFLAIR SNAKE GAME')
screen.setup(width=700,height=700)
screen.tracer(0)
turtle.bgcolor('turquoise')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()

snake =turtle .turtles()
snake.speed(0)
snake.shape('square')
snake.color('black')
snake.penup()
snake.goto(0,0)
snake.direction='stop'

fruit=turtle.turtles()
fruit.speed(0)
fruit.shape('circle')
fruit.colour('red')
fruit.penup()
fruit.goto(30,30)

old_fruit=[]

scoring=turtle.turtle()
scoring.speed(0)
scoring.color("black")
scroing.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.writer("score:",align="center",font=("courier",24,"bold"))
