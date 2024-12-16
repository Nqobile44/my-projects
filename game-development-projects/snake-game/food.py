from turtle import Turtle
import random

# Define the Food class which inherits from the Turtle class
class Food(Turtle):

    # Constructor to initialize the food object
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen so it doesn't leave a trail
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the food smaller (default size is 1)
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the movement speed to the fastest (for instant repositioning)
        self.refresh()  # Call the refresh method to place the food at a random position on screen

    # Method to randomly place the food on the screen
    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate between -280 and 280
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate between -280 and 280
        self.goto(random_x, random_y)  # Move the food to the random coordinates
