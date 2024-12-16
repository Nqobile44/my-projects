from turtle import Turtle  # Import the Turtle class from the turtle module


# Define a Ball class that inherits from the Turtle class
class Ball(Turtle):
    def __init__(self):
        # Initialize the parent class (Turtle)
        super().__init__()

        # Set the color of the ball to white
        self.color("white")

        # Set the shape of the turtle to a circle (representing the ball)
        self.shape("circle")

        # Lift the pen so it doesn't draw lines
        self.penup()

        # Initial movement speed along the Y and X axes
        self.y_move = 1
        self.x_move = 1

        # Initial speed of movement, controlling how fast the ball moves
        self.move_speed = 0.01

    # Method to move the ball
    def move(self):
        # Calculate the new X and Y positions based on the current positions and movement speeds
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # Move the ball to the new position
        self.goto(new_x, new_y)

    # Method to make the ball bounce vertically (reverse its Y-axis movement)
    def bounce_y(self):
        # Reverse the direction of Y-axis movement
        self.y_move *= -1

        # Increase the ball's speed slightly by decreasing move_speed
        self.move_speed *= 0.9

    # Method to make the ball bounce horizontally (reverse its X-axis movement)
    def bounce_x(self):
        # Reverse the direction of X-axis movement
        self.x_move *= -1

    # Method to reset the ball's position to the center of the screen
    def reset_position(self):
        # Move the ball to the center of the screen (coordinates 0, 0)
        self.goto(0, 0)

        # Reset the move speed to the initial value
        self.move_speed = 0.01

        # Reverse the horizontal movement direction
        self.bounce_x()

