from turtle import Screen
from my_snake import Snake
from new_food import SnakeFood
from snake_scoreboard import SnakeScoreboard
import time

snake  = Snake()
snake_food = SnakeFood()
scoreboard = SnakeScoreboard()

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height= 600)
screen.title("The Snake Game.")


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



is_game_stop = True

while is_game_stop:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(snake_food) < 15:
        scoreboard.inrease_score()
        snake_food.recreate()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        is_game_stop = False
        scoreboard.game_over()

    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            is_game_stop = False
            scoreboard.game_over()



screen.exitonclick()