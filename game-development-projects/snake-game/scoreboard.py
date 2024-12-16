from turtle import Turtle

# Constants for text alignment and font used in scoreboard
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

# Read the highest score from a file and store it
with open("data.txt", mode="r") as file:
    highest_score = file.read()

class Score(Turtle):
    def __init__(self):
        # Initialize the Score object by setting up the score properties and appearance
        super().__init__()  # Initialize the Turtle class
        self.score = 0  # Set the current score to 0
        self.high_score = int(highest_score)  # Set the high score from the file (converted to an integer)
        self.color("white")  # Set the text color to white
        self.penup()  # Lift the pen so no lines are drawn while moving
        self.goto(0, 265)  # Position the scoreboard at the top of the screen
        self.update_scoreboard()  # Call method to display the initial scoreboard
        self.hideturtle()  # Hide the turtle cursor (since it is not needed in the scoreboard)

    def update_scoreboard(self):
        # Clear the previous score and update the scoreboard with the current and high scores
        self.clear()  # Clear the previous score
        # Write the updated score and high score to the screen
        self.write(arg=str(f"Score: {self.score} Highest Score: {self.high_score}"), align=ALIGNMENT, font=FONT)

    def gameover(self):
        # Display the game over message at the center of the screen
        self.goto(0, 0)  # Position at the center
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increase the current score by 1 and update the scoreboard
        self.score += 1  # Increase score by 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Update the scoreboard with the new score

    def reset(self):
        # Reset the score and update the high score if necessary
        if self.score > self.high_score:  # Check if current score is higher than the high score
            self.high_score = self.score  # Update the high score
            # Save the new high score to the file
            with open("data.txt", mode="w") as newfile:
                newfile.write(str(self.high_score))

        self.score = 0  # Reset the score to 0
        self.update_scoreboard()  # Update the scoreboard with the reset score


