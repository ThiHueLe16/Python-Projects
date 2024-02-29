from turtle import Turtle
import random
START_POSITION=[(400,100),(400,-170)]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPE=["square", "triangle"]
STARTING_MOVE_DISTANCE = 19
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 12) == 1:
            car = Turtle()
            car_position=random.choice(START_POSITION)
            car_shape=random.choice(SHAPE)
            car.shape(car_shape)
            print(car.shape)

            car.shapesize(stretch_wid=random.randint(1,3), stretch_len=random.randint(1,4))
            car.penup()
            car.goto(car_position)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def mov_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
