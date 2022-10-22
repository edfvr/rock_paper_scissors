import random


player_move = input("Rock, Paper, Scissors? ")

moves = ["rock", "paper", "scissors"]

cpu_move = random.choice(moves)

print(f"You chose {player_move}, cpu chose {cpu_move}.\n")
