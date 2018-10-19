import random

def rock_paper_scissors(user_input, computer_input):
    if user_input _write fitting condition here_:
        return 'tied'

    elif #continue until you have every case covered


if __name__ == "__main__":
    possibilities = ['rock', 'paper', 'scissors']
    for user_choice in possibilities:
        for computer_choice in possibilities:
            if user_choice == computer_choice:
                assert rock_paper_scissors(user_choice, computer_choice) is 'tied'


    for i in range(5):

        userinput = str(input("Choose 'rock', 'paper' or 'scissors': "))
        if userinput in possibilities:
            computer_choice = random.choice(possibilities)
            print(rock_paper_scissors(userinput, computer_choice))

        else:
            print("userinput was not a valid choice!")