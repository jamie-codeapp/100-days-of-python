from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.all_cars = []
        self.car_speed = self.STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(self.COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += self.MOVE_INCREMENT
