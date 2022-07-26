import random
from turtle import Turtle, Screen
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_cor = [0, -20, -40]

segments = []

score = 0

screen.tracer(0)
for position in x_cor:
    timmy = Turtle("square")
    timmy.color("white")
    timmy.penup()
    timmy.goto(position, 0)
    segments.append(timmy)

food = Turtle("circle")

def extend():
    jimmy = Turtle("square")
    jimmy.color("white")
    jimmy.penup()
    segments.append(jimmy)

def foods(food):
    x_food = random.randint(-280, 280)
    y_food = random.randint(-280, 280)
    food.hideturtle()
    food.penup()
    food.color("blue")
    food.goto(x_food, y_food)
    food.showturtle()


def up():
    segments[0].setheading(90)


def down():
    segments[0].setheading(270)


def left():
    segments[0].setheading(180)


def right():
    segments[0].setheading(0)


def keyboard():
    screen.listen()
    screen.onkeyrelease(up, "Up")
    screen.onkeyrelease(down, "Down")
    screen.onkeyrelease(left, "Left")
    screen.onkeyrelease(right, "Right")


def food_collide():
    if segments[0].distance(food) < 20:
        return True


def wall_collide():
    if segments[0].xcor() > 360 or segments[0].xcor() < -360 or segments[0].ycor() > 310 or segments[0].ycor() < -310:
        return True


def own_collide():
    for item in segments[1:]:
        if segments[0].distance(item)<5:
            return True

board = Turtle()

def scoring(score):
    board.clear()
    board.hideturtle()
    board.penup()
    board.goto(0, 280)
    board.color("white")
    board.write(f"Score : {score}", align="center", font=('Arial', 20, 'normal'))

def last():
    over = Turtle()
    over.hideturtle()
    over.penup()
    over.color("yellow")
    over.write("Game Over", align="center", font=('Arial', 20, 'normal'))


scoring(score)
foods(food)
game = True
while game:
    for part in range(1, len(segments)):
        segments[-part].goto(segments[-part-1].pos())
    segments[0].forward(20)
    screen.update()
    time.sleep(0.1)
    keyboard()
    food_collide()
    if food_collide():
        foods(food)
        extend()
        score += 1
        scoring(score)

    if wall_collide():
        game = False
        board = Turtle()
        last()

    if own_collide():
        game = False
        last()







screen.exitonclick()

