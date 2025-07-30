from turtle import Turtle

up = 90
down = 270
right = 0
left = 180

initial_position = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for positon in initial_position:
            self.update_snake(positon)

    def update_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.update_snake(self.snakes[-1].position())

    def move(self):
        for seg in range(len(self.snakes) - 1 , 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def up(self):
        if self.head.heading() != down:
            self.snakes[0].setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.snakes[0].setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.snakes[0].setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.snakes[0].setheading(left)
