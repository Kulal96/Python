from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.update()
        
        self.hideturtle()
    
    def update(self):
        self.goto(0,280)
        self.clear()
        self.write(f"Score :{self.score}", move=False, align='center', font=('Arial', 8, 'normal'))
    
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",move=False, align='center', font=('Arial', 8, 'normal'))

    def scoreincreament(self):
        self.score+=1
        self.update()

        
