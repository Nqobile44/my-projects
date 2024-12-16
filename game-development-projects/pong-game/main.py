import time
from turtle import Turtle, Screen  # Import required modules for graphics and screen setup
from paddle import Paddle  # Import the Paddle class
from ball import Ball  # Import the Ball class
from scoreboard import ScoreBoard  # Import the ScoreBoard class

# Set up the screen with a black background and title
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)  # Set the window size
screen.tracer(0)  # Turn off automatic screen updates to control when it updates

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Right paddle starting at (350, 0)
l_paddle = Paddle((-350, 0))  # Left paddle starting at (-350, 0)
ball = Ball()  # Create a ball object
scoreboard = ScoreBoard()  # Create a scoreboard object

# Set up key listeners for controlling paddles
screen.listen()  # Listen for user input
screen.onkey(fun=r_paddle.go_up, key="Up")  # Right paddle moves up with the "Up" arrow key
screen.onkey(fun=r_paddle.go_down, key="Down")  # Right paddle moves down with the "Down" arrow key
screen.onkey(fun=l_paddle.go_up, key="w")  # Left paddle moves up with the "w" key
screen.onkey(fun=l_paddle.go_down, key="s")  # Left paddle moves down with the "s" key

# The game continues as long as game_is_on is True
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Delay to control the speed of the ball
    screen.update()  # Manually update the screen after each movement
    ball.move()  # Move the ball

    # Bounce the ball when it hits the top or bottom of the screen
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()  # If the ball touches the paddle, bounce it off

    # Check if the ball goes past the right paddle
    if ball.xcor() > 420:
        ball.reset_position()  # Reset the ball to the center
        scoreboard.l_point()  # Award a point to the left player

    # Check if the ball goes past the left paddle
    if ball.xcor() < -420:
        ball.reset_position()  # Reset the ball to the center
        scoreboard.r_point()  # Award a point to the right player

# Wait for the user to click before closing the window
screen.exitonclick()

