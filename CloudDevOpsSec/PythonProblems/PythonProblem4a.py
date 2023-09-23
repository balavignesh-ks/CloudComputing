import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

def get_user_input():
    choice = input(f"\nWhat's your choice ({Action._member_names_})???\n\nEnter '{Action.Rock}' for Rock, '{Action.Paper}' for Paper or '{Action.Scissors}' for Scissors: ")
    user_input = Action(int(choice))
    return user_input

def get_computer_input():
    computer_input = Action(random.randint(1, len(Action)))
    return computer_input

def check_winner(user_input,computer_input):
    if user_input == computer_input:
        print(f"Both user and computer selected '{user_input.name}'. It's a TIE!!!\n")
    elif user_input == Action.Rock:
        if computer_input == Action.Scissors:
            print(f"'{user_input.name}' smashes '{computer_input.name}'! Congrats, You WIN!!!\n")
        else:
            print(f"{computer_input.name} covers '{user_input.name}'! Sorry, You LOSE!!!\n")
    elif user_input == Action.Paper:
        if computer_input == Action.Rock:
            print(f"'{user_input.name}' covers '{computer_input.name}'! Congrats, You WIN!!!\n")
        else:
            print(f"'{user_input.name}' cuts '{computer_input.name}'! Sorry, You LOSE!!!\n")
    elif user_input == Action.Scissors:
        if computer_input == Action.Paper:
            print(f"'{user_input.name}' cuts '{computer_input.name}'! Congrats, You WIN!!!\n")
        else:
            print(f"'{user_input.name}' smashes '{computer_input.name}'! Sorry, You LOSE!!!\n")

def continue_check():
    resp = input("Would you like to play again? (yes/no): ")
    if resp != "yes":
        print(f"\nThank you for playing {Action._member_names_}!!!\n")
        return False