from random import randrange
from freegames import square, vector
from turtle import *

food = vector(10, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# score
score = 0

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'blue')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#pen = turtle.Turtle()
#speed(0)

setup(420, 420, 370, 0)
title("Snake Game!")
hideturtle()
tracer(False)
#shape("square")
#color("black")4
#penup()
#hideturtle()

setposition(130,0)
write("Score: 0", align="right", font=("Courier", 10, "normal"))
#write("Hello!", align="center", font=("Courier", 24, "normal"))
#write("Score: 0 High Score:")

listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
