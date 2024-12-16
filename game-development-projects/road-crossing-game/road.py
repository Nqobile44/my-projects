from turtle import Turtle

# Constants for the position of the road and the color
X_POSITION = 280  # X-coordinate for the start position of the road
Y_POSITION = -260  # Initial Y-coordinate, this is the position that will change after each line


class Road(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the parent Turtle class
        self.color("grey")  # Set the color of the road to grey (this could change)
        self.pensize(3)  # Set the pen size to 3
        self.penup()  # Lift the pen so the turtle does not draw while moving to starting position
        self.y_pos = Y_POSITION  # Set the initial Y-coordinate position for the first line of the road

        self.setheading(180)  # Set the turtle's heading (direction) to 180 degrees (facing left)

        # Loop to draw multiple dashed road lines
        for _ in range(14):  # This loop runs 14 times to draw 14 lines (could represent 14 lanes of the road)
            self.goto(X_POSITION, self.y_pos)  # Move the turtle to the starting position for each line
            for _ in range(30):  # This inner loop draws 30 dashed segments on each line
                self.pendown()  # Lower the pen to draw
                self.forward(10)  # Move the turtle 10 units forward while drawing
                self.penup()  # Lift the pen so the turtle moves without drawing
                self.forward(10)  # Move forward by another 10 units (creating the dashed pattern)

            print(self.ycor())  # Print the current Y-coordinate for debugging
            self.y_pos += 38  # After drawing each line, move the Y-coordinate down by 38 units for the next line
