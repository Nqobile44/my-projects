from turtle import Turtle

# Constants for starting position, movement distance, and finish line
STARTING_POSITION = (0, -280)  # Initial position of the player at the bottom of the screen
MOVE_DISTANCE = 10  # How far the player moves with each step
FINISH_LINE_Y = 280  # The Y-coordinate of the finish line (top of the screen)

class Player:
    def __init__(self):
        super().__init__()  # Call the parent class constructor (not really needed here as there is no custom parent class)
        self.new_move_distance = MOVE_DISTANCE  # Set the initial move distance
        self.player_turtle = Turtle(shape="turtle")  # Create a new turtle object with the shape of a "turtle"
        self.player_turtle.penup()  # Lift the pen so the turtle doesn't draw while moving
        self.player_turtle.goto(STARTING_POSITION)  # Move the player to the starting position
        self.player_turtle.setheading(90)  # Set the turtle to face upwards (90 degrees)

    def go_up(self):
        """Move the player up by the defined move distance."""
        self.player_turtle.forward(MOVE_DISTANCE)

    def new_level(self):
        """Reset the player position to the starting position when they reach the finish line."""
        self.player_turtle.goto(STARTING_POSITION)





