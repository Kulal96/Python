from turtle import Turtle,Screen
import random

screen=Screen()

screen.setup(width=500,height=400)
screen.title("Welcome to the turtle race")
user_guess=screen.textinput("turtle","Who will the race ?")

turtle_colors=['red','green','yellow','orange','purple','blue']
turtle_list=[]
y_index=[-70,-40,-10,20,50,80]

for item in range(6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(turtle_colors[item])
    new_turtle.goto(-230,y_index[item])
    turtle_list.append(new_turtle)

race_on=True

while race_on:
    for new_turtle in turtle_list:
        if new_turtle.xcor() > 230:
            turtle_won_color=new_turtle.fillcolor()
            if turtle_won_color==user_guess:
                print(f"You win! Winning color is {turtle_won_color}")
            else:
                print(f"You lost!")
            race_on=False
        random_distance=random.randint(1,10)
        new_turtle.forward(random_distance)


screen.exitonclick()
