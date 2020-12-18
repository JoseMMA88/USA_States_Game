import turtle
import pandas


FONT = ("Verdana", 9, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
print(state_list)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
guess_states = []


is_game = True
while is_game:
    state = screen.textinput(title=f"{len(guess_states)} / {len(state_list)} States Correct",
                             prompt="What´s another state´s name?").title()

    if state == "Exit":
        is_game = False
        missing_states = [state for state in state_list if state not in guess_states]
        out_data = pandas.DataFrame(missing_states)
        out_data.to_csv("to_learn.csv")

    if state in state_list and state not in guess_states:
        guess_states.append(state)
        data_aux = data[data["state"] == state]
        x = int(data_aux["x"])
        y = int(data_aux["y"])
        pen.goto(x, y)
        pen.write(arg=state, font=FONT)
