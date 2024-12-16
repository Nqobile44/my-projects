from turtle import Turtle

# Font settings for displaying the score and game over message
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Call the parent class's initialization method
        self.score = 0  # Initial score is set to 0
        self.penup()  # Lift the pen so that no drawing lines are left behind
        self.score_tracker()  # Display the score tracker
        self.hideturtle()  # Hide the Turtle object after drawing the score

    def score_tracker(self):
        # Position the scoreboard at (-140, 250) on the screen
        self.setpos(-140, 250)
        self.clear()  # Clear any previous score before writing the new score
        # Write the current score (level) on the screen
        self.write(arg=f"Level: {self.score}", align="right", font=FONT)

    def game_over(self):
        # Display the "Game Over" message at the center of the screen
        self.setpos(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)

