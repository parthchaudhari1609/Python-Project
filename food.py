from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.color("green")
        self.refresh()

    def refresh(self):
        x_position = random.randint(-270, 270)
        y_position = random.randint(-270, 270)
        self.goto(x=x_position, y=y_position)