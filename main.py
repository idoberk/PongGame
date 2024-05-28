import time
from paddle import Paddle
from turtle import Screen
from ball import Ball
from score_board import Field, ScoreBoard

SCREEN_SIZE = [800, 600]
SCREEN_BOUNDARIES = 280
PADDLE_COORDS = [(-350, 0), (350, 0)]

screen = Screen()
screen.setup(width = SCREEN_SIZE[0], height = SCREEN_SIZE[1])
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
field = Field()
score = ScoreBoard()

left_paddle = Paddle(PADDLE_COORDS[0])
right_paddle = Paddle(PADDLE_COORDS[1])

game_ball = Ball()

screen.listen()
screen.onkey(key = "Up", fun = right_paddle.move_paddle_up)
screen.onkey(key = "Down", fun = right_paddle.move_paddle_down)
screen.onkey(key = "w", fun = left_paddle.move_paddle_up)
screen.onkey(key = "s", fun = left_paddle.move_paddle_down)

game_is_on = True

while game_is_on:
    time.sleep(game_ball.ball_speed)
    screen.update()
    game_ball.move_ball()

    # Detect if ball hits the walls.
    if game_ball.ycor() > SCREEN_BOUNDARIES or game_ball.ycor() < -SCREEN_BOUNDARIES:
        game_ball.top_bottom_wall_bounce()

    # Detect if paddles hit the ball.
    if ((game_ball.distance(left_paddle) < 54 and -320 > game_ball.xcor() > -350) or
            (game_ball.distance(right_paddle) < 54 and 350 > game_ball.xcor() > 320)):
        game_ball.paddle_bounce()

    # Detect if right player missed the ball.
    if game_ball.xcor() > 400:
        game_ball.goal()
        score.increase_l_player_score()

    # Detect if left player missed the ball.
    if game_ball.xcor() < -400:
        game_ball.goal()
        score.increase_r_player_score()

screen.exitonclick()