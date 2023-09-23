from PythonProblem4a import *

check = True

while check:
    try:
        user_input = get_user_input()
    except ValueError as error:
        input_range = f"[1,{len(Action)}]"
        print(f"Invalid selection. Enter a value in range {input_range} \n")
        continue 

    computer_input = get_computer_input()
    print(f"\nYou chose {user_input.name}, computer chose {computer_input.name}.\n")
    check_winner(user_input,computer_input)

    check = continue_check()