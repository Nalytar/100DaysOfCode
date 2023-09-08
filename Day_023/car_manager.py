from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
NUMBER_OF_CARS = 30


class CarManager:
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []

        self.generate_cars()

    def generate_cars(self):
        # Generate Cars on x_value
        for _ in range(0, NUMBER_OF_CARS):
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(random.randint(-360, 360), random.randint(-12, 14) * 20)
            self.cars.append(new_car)

    def cars_start(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def replace_cars(self):
        for car in self.cars:
            if car.xcor() < -400:
                car.goto(320, random.randint(-12, 14) * 20)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 25:
                return True
        return False
