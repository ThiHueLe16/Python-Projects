# Game about guessing all the state name in america. when type "exit", return a csv file to
# show all missing states which the player didn't manage to guess
import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv("50_states.csv")
guess_state = []
game_continue=True
while len(guess_state)<50 and game_continue:
    answer = turtle.textinput(title=f"{len(guess_state)}/50:States Correct", prompt="What is another State's name")
    answer= answer.title()
    print(answer)
    states_name_list = data_states.state.to_list()
    if answer=="Exit":
        game_continue=False
        missing_states=[]
        for s in states_name_list:
            if s not in guess_state:
                missing_states.append(s)
        missing_states_df= pandas.DataFrame(missing_states)
        missing_states_df.to_csv("missingstates.csv")

    if answer in states_name_list:
        guess_state.append(answer)
        print(guess_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data_states[data_states.state == answer]
        tim.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        tim.write(answer)

