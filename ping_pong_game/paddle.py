from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position,0)
    
    def Up(self):
        new_x=self.xcor()
        new_y=self.ycor()+15
        self.goto(new_x,new_y)

    def Down(self):
        new_x=self.xcor()
        new_y=self.ycor()-15
        self.goto(new_x,new_y)
