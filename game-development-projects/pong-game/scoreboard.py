from turtle import Turtle  # Import the Turtle class from the turtle module


# Define a ScoreBoard class that inherits from the Turtle class
class ScoreBoard(Turtle):
    # Initialize the scoreboard
    def __init__(self):
        # Initialize the parent class (Turtle)
        super().__init__()

        # Set the color of the scoreboard text to white
        self.color("white")

        # Lift the pen so it doesn't draw lines
        self.penup()

        # Hide the turtle (the object won't be visible during the game)
        self.hideturtle()

        # Initialize the left and right scores to 0
        self.l_score = 0
        self.r_score = 0

        # Call the method to update the scoreboard display
        self.update_scoreboard()

    # Method to update the scoreboard display
    def update_scoreboard(self):
        # Clear the previous score display before updating
        self.clear()

        # Position the turtle to display the left player's score (-100, 200)
        self.goto(-100, 200)

        # Write the left player's score on the screen, centered, with large font
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

        # Position the turtle to display the right player's score (100, 200)
        self.goto(100, 200)

        # Write the right player's score on the screen, centered, with large font
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Method to increase the left player's score by 1 point
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()  # Update the scoreboard after the point

    # Method to increase the right player's score by 1 point
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()  # Update the scoreboard after the point
