from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

game_on=True
screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        score.scoreincreament()
        snake.extend()
    
    if snake.head.distance(snake.segments[-1]) < 10 :
        game_on=False
        score.gameover()

    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on=False


screen.exitonclick()

