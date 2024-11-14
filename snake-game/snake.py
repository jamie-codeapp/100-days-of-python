from turtle import Turtle


class Snake:

    def __init__(self):
        self.STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.MOVE_DISTANCE = 20
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)
