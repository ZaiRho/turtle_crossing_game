from turtle import Turtle


class LevelManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Level : {self.level}", True, "center", ("courier", 18, "normal"))

    def add_level(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, "center", ("courier", 40, "bold"))
