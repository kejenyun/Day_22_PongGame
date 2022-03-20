
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')


# create a paddle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

#create movement
    def go_up(self):
        self.penup()
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        self.penup()
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
