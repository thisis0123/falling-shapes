from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.up()
        self.hideturtle()
        self.color("white")
        self.goto(0,250)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("courier",20,"bold"))
    

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("courier",30,"bold"))
