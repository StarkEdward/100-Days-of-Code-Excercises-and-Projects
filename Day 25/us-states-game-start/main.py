import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []

# get the co-ordinate
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    # if answer_state is one of the state in all the states of the 50_states.csv.
    if answer_state == "Exit":  # exit the game when type exit
        missing_states = [state for state in all_state if state not in guessed_state]
        # missing_states = []
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))  # if they got it right
        # create a turtle to write the name of the state at the state's x and y co-ordinates.
        # t.write(state_data.state.item())
        t.write(answer_state)


