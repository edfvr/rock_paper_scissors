import random
from enum import IntEnum

class Move(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

victories = {
        Move.Rock: [Move.Scissors],
        Move.Paper: [Move.Rock],
        Move.Scissors: [Move.Paper]
    }

def get_player_choice():
    arsenal = [f"{move.name}[{move.value}]" for move in Move]
    move_list_str = ", ".join(arsenal)
    choice = int(input(f"Rock Paper Scissors? ({move_list_str})"))
    move = Move(choice)
    return move

def get_cpu_choice():
    choice = random.randint(0, len(Move) - 1)
    move = Move(choice)
    return move

# Conditions for winning
def determine_winner(player_move, cpu_move):
    defeats = victories[player_move]
    if player_move == cpu_move:
        print(f"Both players selected {player_move.name}. Tie!")
    elif cpu_move in defeats:
        print(f"{player_move.name} beats {cpu_move.name}! You win!")
    else:
        print(f"{cpu_move.name} beats {player_move.name}! SIT DOWN! You lose!")

while True:
    try:
        player_move = get_player_choice()
    except ValueError as e:
        range_str = f"[0, {len(Move) - 1}]"
        print(f"Enter a value in range")
        continue
    
    cpu_move = get_cpu_choice()
    determine_winner(player_move, cpu_move)

    replay = input("Another go? (y/n): ")
    if replay == 'n':
        break
    if replay == 'y':
        continue