from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PINGPONG")

screen.tracer(0)

r_paddle=Paddle(360)
l_paddle=Paddle(-360)
ball=Ball()
scoreboard=Scoreboard()

game_on=True

screen.listen()

screen.onkey(r_paddle.Up,"Up")
screen.onkey(l_paddle.Up,"w")
screen.onkey(r_paddle.Down,"Down")
screen.onkey(l_paddle.Down,"s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290 :
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()
    
    if ball.xcor() < -380 :
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()
