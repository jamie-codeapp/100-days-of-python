from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(self.MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(self.STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > self.FINISH_LINE_Y:
            return True
        return False
