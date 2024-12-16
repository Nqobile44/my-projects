from turtle import Turtle

# Constants defining the starting positions of the snake's segments and movement directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake's body segments
MOVE_DISTANCE = 20  # Distance the snake moves each time
UP = 90  # Angle for upward movement (in degrees)
DOWN = 270  # Angle for downward movement (in degrees)
LEFT = 180  # Angle for leftward movement (in degrees)
RIGHT = 0  # Angle for rightward movement (in degrees)

class Snake:
    # Snake class to create and manage the snake's movement and growth
    def __init__(self):
        self.segments = list()  # List to store the segments of the snake
        self.create_snake()  # Calls method to create the snake with initial segments
        self.head = self.segments[0]  # The head of the snake is the first segment in the list

    def create_snake(self):
        # Create the initial snake using the predefined starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Adds a segment at each starting position

    def add_segment(self, position):
        # Add a new segment to the snake at the specified position
        snake_bar = Turtle(shape="square")  # Create a new turtle object for the segment
        snake_bar.color("White")  # Set the color of the segment to white
        snake_bar.penup()  # Lift the pen so it doesn't leave a trail
        snake_bar.setpos(position)  # Set the position of the segment
        self.segments.append(snake_bar)  # Append the new segment to the list of segments

    def reset(self):
        # Reset the snake to its initial state when the game is over
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move all segments off-screen (out of view)
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Create a new snake with the initial segments
        self.head = self.segments[0]  # Set the head to the first segment in the new snake

    def extend(self):
        # Add a new segment to the snake's body
        self.add_segment(self.segments[-1].position())  # Add a segment at the position of the last segment

    def snake_move(self):
        # Move the snake forward by updating each segment's position
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment and move backwards
            # Get the position of the segment in front of the current segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to that position
        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward

    def up(self):
        # Change the direction of the snake to up if it's not already heading down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the direction of the snake to down if it's not already heading up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the direction of the snake to left if it's not already heading right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the direction of the snake to right if it's not already heading left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




