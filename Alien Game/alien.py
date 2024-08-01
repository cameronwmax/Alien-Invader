from turtle import *


class Alien(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("arrow")
        self.color("green")
        self.shapesize(2, 2, 0)
        self.right(90)
        self.penup()
        self.goto(x, y)
        self.x_move = 5
        

    def remove_alien(self, aliens:list):
        """Function to remove alien form screen and list"""
        self.hideturtle()
        self.clear()
        aliens.remove(self)

    
    def move_alien(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
        
    
    def change_dir(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
        self.x_move *= -1