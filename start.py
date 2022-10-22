import random


player_move = input("rock, paper, scissors? ")

moves = ["rock", "paper", "scissors"]

cpu_move = random.choice(moves)

print(f"You chose {player_move}, cpu chose {cpu_move}.\n")

if player_move == cpu_move:
    print(f"We both selected {player_move}. Tie!")
elif player_move == "rock" and cpu_move == "scissors":
    print("Rock smashes scissors! You win!")
elif player_move == "rock" and cpu_move == "paper":
    print("Paper covers rock! SIT DOWN!! I win")
elif player_move == "paper" and cpu_move == "rock":
    print("Paper covers rock! You win!")
elif player_move == "paper" and cpu_move == "scissors":
    print("Scissors cuts paper! HAHA I win!")
elif player_move == "scissors" and cpu_move == "paper":
    print("Scissors cuts paper! You win you lucky bastard!")
elif player_move == "scissors" and cpu_move == "rock":
    print('Rock smashes scissors! I win! I "trashes" you!')