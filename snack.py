from turtle import Turtle

up = 90
down = 270
right = 0
left = 180
initial_position = [(0, 0), (-20, 0), (-40, 0)]

class Snack:


    def __init__(self):
        self.snacks = []
        self.create_snack()
        self.head = self.snacks[0]

    def create_snack(self):
        for position in initial_position:
            self.add_snack(position)

    def add_snack(self, position):
        new_snack = Turtle("square")
        new_snack.color("white")
        new_snack.penup()
        new_snack.goto(position)
        self.snacks.append(new_snack)

    def extend(self):
        self.add_snack(self.snacks[-1].position())


    def move(self):
        for sna in range(len(self.snacks) - 1, 0, -1):

            new_x = self.snacks[sna - 1].xcor()
            new_y = self.snacks[sna - 1].ycor()
            self.snacks[sna].goto(new_x, new_y)
        self.snacks[0].forward(20)

    def up(self):
        if self.head.heading() != down:
         self.snacks[0].setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.snacks[0].setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.snacks[0].setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.snacks[0].setheading(right)