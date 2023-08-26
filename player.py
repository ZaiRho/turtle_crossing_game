from turtle import Turtle

STARTING_POSITION = (0,-280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(20)

    def add_level(self):
        self.goto(STARTING_POSITION)

