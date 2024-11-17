from turtle import Turtle
import random

class FallingShape(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shapes=("circle","square","triangle","turtle")
        self.colors=("yellow","DarkGreen","MediumBlue","Gold","Maroon","MediumVioletRed","Red","Tan")
        self.reset_position()
        

    def reset_position(self):
        self.shape(random.choice(self.shapes))

        #creating a 50% chance for a white turtle to emerge
        if self.shape()=="turtle" and random.randint(0,1)==1:
            self.color("white")
        else:
            self.color(random.choice(self.colors))

        
        self.x_cor=random.randint(-360,360)
        self.y_cor=310
        self.goto(self.x_cor,self.y_cor)

    def move(self):
        self.y_cor-=10
        self.goto(self.x_cor,self.y_cor)
        

         
