from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.goto(0,-250)
        self.shapesize(stretch_len=5,stretch_wid=1)

    def move_right(self):
        new_x=self.xcor()+20
        if new_x < 350:
            self.goto(new_x,self.ycor())
    
    def move_left(self):
        new_x=self.xcor()-20
        if new_x >-350:
         self.goto(new_x,self.ycor())
    