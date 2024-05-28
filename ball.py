from turtle import Turtle

STARTING_POS = (0, 0)

class Ball(Turtle):

    def __init__(self):
        """Ball class constructor."""
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def create_ball(self):
        """Creates the ball."""
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POS)

    def move_ball(self):
        """Moves the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def top_bottom_wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def goal(self):
        self.goto(STARTING_POS)
        self.ball_speed = 0.1
        self.paddle_bounce()