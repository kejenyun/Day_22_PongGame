from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard


screen = Screen()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collisions with the top (y = 280) and bottom walls (y = -280), because the width of the ball is 20
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

        # detect R-out of bound
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect L-out of bound
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()






screen.exitonclick()