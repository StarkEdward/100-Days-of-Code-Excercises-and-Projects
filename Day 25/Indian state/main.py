# 03/08/2022    @ Sagar Kamble
# Guess the Indian State Quiz
import turtle
import pandas

screen = turtle.Screen()
screen.title("States of India")
image = "Indian_states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("29_indian_states.csv")
all_states = data.state.to_list()  # convert all states into list
guessed_state = []  # create a empty list to store correct guess

while len(guessed_state) < 29:  # go through all the states in list.
    answer_state = screen.textinput(title=f"{len(guessed_state)} / 29 Guess the State!",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":  # exit from loop when type exit and close the application.
        # create missing_state.csv to learn the state
        missing_states = []  # empty list for missing states
        for state in all_states:  # go through all the states list
            if state not in guessed_state:  # check state is not guessed state
                missing_states.append(state)  # and append the state in missing state
        new_data = pandas.DataFrame(missing_states)  # create pandas data to store missing states
        new_data.to_csv("State_Missed.csv")  # and create a csv file to store
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)  # append  answer_state to guessed_state
        t = turtle.Turtle()  # create turtle to show on map
        t.hideturtle()  # hide turtle shape
        t.penup()  # avoid drawing
        state_data = data[data.state == answer_state]  # if answer state is equal to state in csv file we can
        # get a row of particular state like x, y co-ordinates
        t.goto(int(state_data.x), int(state_data.y))  # get the value of x and y from csv for particular state and
        # print on perfect location where the x, y co-ordinates are provided.
        t.write(answer_state)  # then write the answer_state.
