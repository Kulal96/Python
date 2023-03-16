from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-10,0),(-20,0)]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    
    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head=self.segments[0]
            
    
    def addsegment(self,position):
        new_segment =Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.addsegment(self.segments[-1].position())

    
    def movesnake(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num -1].xcor()
            new_y=self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(10)
        # self.head.left(90)
    
    def Up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def Left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)


