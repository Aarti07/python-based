import turtle
import random
import time


screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("yellow")


turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()
Score = 0
delay = 0.1

snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("pink")
food.penup()
food.goto(30, 30)

old_food = []


score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 300)
score.write("Score: ", align="center", font=("Courier", 24, "bold"))


def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def move():
    if snake.direction == "Up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "Down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "Left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "Right":
        x = snake.xcor()
        snake.setx(x + 20)


screen.listen()
screen.onkeypress(snake_go_down, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

while True:
    screen.update()
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        score.clear()
        score += 1
        score.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("orange")
        new_food.penup()
        old_food.append(new_food)
    for index in range(len(old_food)-1, 0, -1):
        a = old_food[index-1].xcor()
        b = old_food[index-1].ycor()

        old_food[index].goto(a, b)

    if len(old_food) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a, b)
    move()

    if snake.xcor() > 280 or snake.xcor() > -300 or snake.ycor() > 240 or snake.ycor() > -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("violet")
        score.goto(0, 0)
        score.write("    Game Over  \n Your Score is {}".format(score), align="center", font=("Courier", 24, "bold"))

    for food in old_food:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("violet")
            score.goto(0, 0)
            score.write("Game Over  \n Your Score is {}".format(score), align="center", font=("Calibri", 24, "bold"))
    time.sleep(delay)
