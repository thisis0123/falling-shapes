from turtle import Turtle, Screen
from paddle import Paddle
from score import Scoreboard
from falling_shape import FallingShape
import time


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("falling shapes")


screen.tracer(0)
paddle=Paddle()
score=Scoreboard()
falling_shape=FallingShape()


screen.listen()
screen.onkey(paddle.move_right,"Right")
screen.onkey(paddle.move_left,"Left")

falling_shape_sleep=0.1
game_on=True

while game_on:

    while falling_shape.y_cor>-300:

        screen.update()
        time.sleep(falling_shape_sleep)
        falling_shape.move()
        

        if falling_shape.y_cor<=-230 and falling_shape.distance(paddle)<=50:
            if falling_shape.shape()=="circle":
                score.score+=1

            elif falling_shape.shape()=="square":
                score.score+=2

            elif falling_shape.shape()=="triangle":
                score.score=0
                
            elif falling_shape.shape()=="turtle":
                if falling_shape.fillcolor()=="white":
                    score.game_over()  
                    game_on=False
                    break

                else:
                    score.score+=5
            

            score.update_score()
            break
    
    falling_shape.reset_position()

    



screen.exitonclick()

