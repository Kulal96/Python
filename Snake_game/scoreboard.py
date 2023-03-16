from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("d:/Python/Day_32_snake_practice/data.txt","r") as f:
            self.highscore=int(f.read())
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.displayscore()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("d:/Python/Day_32_snake_practice/data.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.displayscore()
        
    
    def displayscore(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}",align="left", font=("Arial", 8, "normal"))
        self.hideturtle()
    
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"Game OVer!!",align="left", font=("Arial", 8, "normal"))
    
    def updatescore(self):
        self.score+=1
        self.displayscore()