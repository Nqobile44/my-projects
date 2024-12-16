from turtle import Turtle  # Import the Turtle class from the turtle module


# Define a Paddle class that inherits from the Turtle class
class Paddle(Turtle):
    # Initialize the paddle with a specific position
    def __init__(self, position):
        # Initialize the parent class (Turtle)
        super().__init__()

        # Set the color of the paddle to white
        self.color("white")

        # Set the shape of the paddle to a square
        self.shape("square")

        # Stretch the paddle's shape to make it longer vertically (5x1)
        self.shapesize(stretch_wid=5, stretch_len=1)

        # Lift the pen so it doesn't leave a trail
        self.penup()

        # Set the paddle to the provided position (tuple containing x and y coordinates)
        self.setpos(position)

    # Method to move the paddle up
    def go_up(self):
        # Calculate the new y-coordinate by adding 20 units to the current y-coordinate
        new_y = self.ycor() + 20

        # Move the paddle to the new position, keeping the x-coordinate the same
        self.goto(self.xcor(), new_y)

    # Method to move the paddle down
    def go_down(self):
        # Calculate the new y-coordinate by subtracting 20 units from the current y-coordinate
        new_y = self.ycor() - 20

        # Move the paddle to the new position, keeping the x-coordinate the same
        self.goto(self.xcor(), new_y)



