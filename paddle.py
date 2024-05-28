from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1

class Paddle(Turtle):

    def __init__(self, position):
        """Paddle class constructor."""
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """Creates the paddle."""
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.goto(position)

    def move_paddle_up(self):
        """Function to move the paddle up."""
        if self.ycor() < 241:
            y_coord_move = self.ycor() + MOVE_DISTANCE
            x_coord_move = self.xcor()
            self.goto(x_coord_move, y_coord_move)

    def move_paddle_down(self):
        """Function to move the paddle down."""
        if self.ycor() > -230:
            y_coord_move = self.ycor() - MOVE_DISTANCE
            x_coord_move = self.xcor()
            self.goto(x_coord_move, y_coord_move)