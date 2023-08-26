from turtle import Turtle
import random
COLORS = ["green", "white", "yellow", "orange", "red", "blue", "purple", "coral"]


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self, car_count):
        for i in range(car_count):
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.seth(180)
            new_car.goto(random.randint(320, 920), random.randint(-240, 240))
            self.cars.append(new_car)

    def move_forward(self):
        for car in self.cars:
            if car.xcor() < -320:
                y_random = random.randint(-240, 240)
                x_random = random.randint(320, 920)
                car.goto(x_random, y_random)
            car.forward(20)

    def add_level(self, num):
        self.create_car(num)

    def give_distance(self):
        distances = []
        for car in self.cars:
            distances.append(car.pos())
        return distances
