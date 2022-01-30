import turtle

import pandas
import pandas as pd

data = pd.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = data.state.to_list()
count = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{count}/50 states. ", prompt=f"Name a state:  ").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.values:
        guessed_states.append(answer_state)
        state_xy = data[data.state == answer_state]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(int(state_xy.x), int(state_xy.y))
        state.write(f"{answer_state}", align='center', font=("Arial", 12, "normal"))
        count += 1

turtle.mainloop()
