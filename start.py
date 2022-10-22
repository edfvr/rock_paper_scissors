import random
from enum import IntEnum

class Action(IntEnum):
        Rock = 0
        Paper = 1
        Scissors = 2

def get_player_choice():
    arsenal = [f"{move.name}[{move.value}]" for move in Action]
    move_list_str = ", ".join(arsenal)
    choice = int(input(f"Rock Paper Scissors ({move_list_str})?"))
    move = Action(choice)
    return move

def get_cpu_choice():
    choice = random.randint(0, len(Action) - 1)
    move = Action(choice)
    return move

# Conditions for winning
def determine_winner(player_move, cpu_move):
    if player_move == cpu_move:
        print(f"We both selected {player_move}. Tie!")

    elif player_move == Action.Rock and cpu_move == Action.Scissors:
        print("Rock smashes scissors! You win!")
    elif player_move == Action.Rock and cpu_move == Action.Paper:
        print("Paper covers rock! SIT DOWN!! I win")

    elif player_move == Action.Paper and cpu_move == Action.Rock:
        print("Paper covers rock! You win!")
    elif player_move == Action.Paper and cpu_move == Action.Scissors:
        print("Scissors cuts paper! HAHA I win!")

    elif player_move == Action.Scissors and cpu_move == Action.Paper:
        print("Scissors cuts paper! You win you lucky ...!")
    elif player_move == Action.Scissors and cpu_move == Action.Rock:
        print('Rock smashes scissors! I win! I "trashes" you!')

while True:
    try:
        player_move = get_player_choice()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Enter a value in range")
        continue
    
    cpu_move = get_cpu_choice()
    determine_winner(player_move, cpu_move)

    replay = input("Another go? (y/n): ")
    if replay == 'n':
        break
    if replay == 'y':
        continue

get_player_choice()
get_cpu_choice()
determine_winner(Action.Rock, Action.Scissors)