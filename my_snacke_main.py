from  turtle import Screen
from snack import Snack
import time
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
snack = Snack()
food = Food()
screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The snack game.")


screen.listen()

screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")

is_game_continue = True
while is_game_continue:
    screen.update()
    time.sleep(0.2)
    snack.move()
    # Detect collision with food
    if snack.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snack.extend()

    #Detect collision with wall

    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        scoreboard.game_over()
        is_game_continue = False


    for san in snack.snacks[1:]:
        if snack.head.distance(san) < 10:
            is_game_continue = False
            scoreboard.game_over()



screen.exitonclick()