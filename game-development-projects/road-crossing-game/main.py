import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
road = Road()

screen.onkey(fun=player.go_up, key="Up")
car_movement = 10
score = Scoreboard()
game_is_on = True
not_crush = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if not_crush:
        car_manager.create_car()
        car_manager.move_cars()

    # Detect if player reaches the finish line (top of the screen)
    if player.player_turtle.ycor() >= 290:  # Check if the player's Y-coordinate is at the finish line
        player.new_level()
        car_manager.level_up()
        score.score += 1
        score.score_tracker()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if player.player_turtle.distance(car) < 20:  # Check if the player collides with a car
            score.game_over()
            not_crush = False  # Stop the game if the player collides with a car

screen.exitonclick()




