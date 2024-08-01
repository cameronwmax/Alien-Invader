from turtle import *


class Ship(Turtle):
    """Class to manage ship attributes"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shapesize(4, 4, 0)
        self.left(90)
        self.reset_ship()

    def move_left(self):
        """Function to move the ship left"""
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
        
    
    def move_right(self):
        """Function to move the ship right"""
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    
    def reset_ship(self):
        """Function to reset the ship to starting point"""
        self.goto(0, -240)