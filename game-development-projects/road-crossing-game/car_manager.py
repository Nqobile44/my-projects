from turtle import Turtle
import random

# List of possible y-positions for cars to appear on
lanes_pos = [216, 178, 140, 102, 64, 26, -12, -50, -88, -126, -164, -202]

# List of colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Starting move distance and increment for car speed
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = list()  # List to hold all the car objects
        self.move_distance = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        # Random chance to create a new car (1 out of 6)
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")  # Create a new car (Turtle object)
            new_car.shapesize(stretch_wid=1.3, stretch_len=2)  # Resize the car shape
            new_car.penup()  # Lift the pen so the car doesn't leave trails
            new_car.color(random.choice(COLORS))  # Random color for the car
            # Randomly select a y-position from the lanes_pos list
            random_y = random.choice(lanes_pos)
            new_car.goto(300, random_y)  # Position the car at the far right of the screen
            self.all_cars.append(new_car)  # Add the new car to the all_cars list

    def move_cars(self):
        # Move each car in the all_cars list backwards
        for car in self.all_cars:
            car.backward(self.move_distance)

    def level_up(self):
        # Increase the speed of the cars as the level progresses
        self.move_distance += MOVE_INCREMENT


