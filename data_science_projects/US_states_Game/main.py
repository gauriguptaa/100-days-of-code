import turtle
import pandas

if __name__ == '__main__':
    # Basic Setup
    screen = turtle.Screen()
    screen.title("US Quiz Project")
    screen.bgpic("blank_states_img.gif")
    turtle.hideturtle()
    turtle.penup()
    state_file = pandas.read_csv("50_states.csv")
    guessed_state = []

    # Comparing user's input with csv file
    while len(guessed_state) < 50:
        user_state_input = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                            prompt="What's another state name").title()
        if user_state_input == "Exit":
            break
        if user_state_input in state_file.state.to_list() and user_state_input not in guessed_state:
            guessed_state.append(user_state_input)
            state_data = state_file[state_file["state"] == user_state_input]
            turtle.setposition(int(state_data.x), int(state_data.y))
            turtle.write(state_data.state.item())

    # states that have not been guessed are put into a csv file for learning
    states_to_learn = []
    for state in state_file.state.to_list():
        if state not in guessed_state:
            states_to_learn.append(state)

    df = pandas.DataFrame({"states_to_learn": states_to_learn})
    df.to_csv("states_to_learn.csv")

