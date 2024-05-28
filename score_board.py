from turtle import Turtle

L_PLAYER_SCORE_COORDS = (-100, 200)
R_PLAYER_SCORE_COORDS = (100, 200)
SCORE_FONT = ("Courier", 80, "normal")
FIELD_ALIGN = "center"
COLOR = "white"

class ScoreBoard(Turtle):

    def __init__(self):
        """ScoreBoard class constructor."""
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.pencolor(COLOR)
        self.penup()
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(R_PLAYER_SCORE_COORDS)
        self.write(arg = f"{self.r_score}", move = False, align = FIELD_ALIGN, font = SCORE_FONT)
        self.goto(L_PLAYER_SCORE_COORDS)
        self.write(arg = f"{self.l_score}", move = False, align = FIELD_ALIGN, font = SCORE_FONT)

    def increase_l_player_score(self):
        self.l_score += 1
        self.update_score_board()

    def increase_r_player_score(self):
        self.r_score += 1
        self.update_score_board()

class Field(Turtle):

    def __init__(self):
        """Field class constructor."""
        super().__init__()
        self.draw_field()

    def draw_field(self):
        self.hideturtle()
        self.pensize(5)
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        self.pencolor(COLOR)
        for y_coord in range(300, -330, -30):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
