from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# Set up the screen for the game
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size to 600x600 pixels
screen.bgcolor("black")  # Set the background color to black
screen.title("My snake Game")  # Set the title of the game window
screen.tracer(0)  # Turn off automatic screen updates to manually control when it updates

# Create instances of Snake, Food, and Score objects
snake = Snake()
segments = snake.segments  # Access the segments of the snake (head and body)
food = Food()  # Create the food object
score = Score()  # Create the scoreboard object

# Start the game
game_is_on = True
screen.listen()  # Start listening for key presses

while game_is_on:
    screen.update()  # Update the screen manually
    time.sleep(0.1)  # Add a delay to control the snake's speed

    # Move the snake
    snake.snake_move()

    # Set up key bindings to control the snake's direction
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    # Detect collision with food
    if snake.head.distance(food) <= 15:  # If the head of the snake is close enough to the food
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Add a new segment to the snake
        score.increase_score()  # Increase the score by 1

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # If the snake hits the wall (x or y coordinates out of bounds)
        score.reset()  # Reset the score
        snake.reset()  # Reset the snake to its starting position

    # Detect collision with the snake's tail
    for segment in snake.segments[1:]:  # Loop through all segments of the snake's body except the head
        if snake.head.distance(segment) < 10:  # If the head is too close to any body segment
            score.reset()  # Reset the score
            snake.reset()  # Reset the snake to its starting position

# Exit the game when the screen is clicked
screen.exitonclick()
