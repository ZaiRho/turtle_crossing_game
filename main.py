from turtle import Screen
from player import Player
from car_manager import CarManager
from level_manager import LevelManager
import time

game_over = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
level_manager = LevelManager()
car_manager.create_car(level_manager.level * 2)
screen.listen()
screen.onkey(player.move_up, "w")


def add_level():
    player.add_level()
    level_manager.add_level()
    car_manager.add_level(level_manager.level * 2)
    time.sleep(1)


def check_collision():
    distance = car_manager.give_distance()
    for i in distance:
        if player.distance(i) < 20:
            return True


while not game_over:
    screen.update()
    car_manager.move_forward()
    if player.ycor() > 240:
        add_level()
        print("Level Completed")
    if check_collision():
        level_manager.game_over()
        game_over = True
    time.sleep(0.1)

screen.exitonclick()
