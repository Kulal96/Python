import turtle
import pandas

screen=turtle.Screen()
screen.title("US-State_game")
image="d:/Python/Day_35/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
guessed_states=[]
count=0


while len(guessed_states)<=50:

    user_guess=screen.textinput(title=f"{count}/50 states correct",prompt='Guess the state name ?')
    u_user_input=user_guess.title()
    data=pandas.read_csv("d:/Python/Day_35/50_states.csv")
    state_list=data.state.tolist()
    
    if u_user_input=='Exit':
        missing_state=[]
        for state in state_list:
            if state not in guessed_states:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("d:/Python/Day_35/missing_states.csv")
        break
        
    if u_user_input in state_list:
        t=turtle.Turtle()
        t.color('black')
        t.hideturtle()
        t.penup()
        state_data=data[data.state==u_user_input]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(u_user_input)
        count+=1
    


        

#turtle.mainloop()