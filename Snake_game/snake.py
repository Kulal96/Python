from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-10,0),(-20,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    
    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)
    
    def addsegment(self,position):
        new_segment=Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.addsegment(self.segments[-1].position())
    
    def move(self):
          for segment in range(len(self.segments)-1,0,-1):
            new_x= self.segments[segment - 1].xcor()
            new_y= self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x,new_y)
          self.head.forward(10)
          #self.segments[0].left(90)
    
    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def Down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def Left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def Right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
