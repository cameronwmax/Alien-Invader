from turtle import *


class Bullet(Turtle):
    def __init__(self, ship):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(1, .25, 0)
        self.penup()
        self.start_point(ship)
        

    def start_point(self, ship:object):
        """Function for starting bullet pos"""
        self.goto(ship.xcor(), ship.ycor())


    def move_bullet(self):
        """Function to move the bullet upwards"""
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)


    def remove_bullet(self, bullets:list):
        bullets.remove(self)
        self.hideturtle()
        self.clear()

    