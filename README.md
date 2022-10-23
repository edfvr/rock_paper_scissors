# Rock Paper Scissors
A simple game

*rock smashes scissors, paper covers rock, scissors cuts paper*

## Pseudocode
- ### Take user input and store.
- Make a list of moves. i.e `["rock", "paper", "scissors"]`
- Use `random.choice()` on `cpu_move` so that the computer selects moves randomly.
    - import `random` to be able to use `random.choice()`
- print `user_move` and `cpu_move` to update user
- ### Determine winner
- Set conditions for winning *(rock smashes scissors, paper covers rock, scissors cuts paper)*
    - if player = cpu, it's a tie
    - if player = rock and cpu = scissors, player wins
        else if cpu = paper, cpu wins
    - if player = paper and cpu = rock, player wins
        else if cpu = scissors, cpu wins
    - if player = scissors and cpu = paper, player wins
        else if cpu = rock, cpu wins
- Loop game, asking user if to continue after every round
- Assign each move a number so that you can reference.
- Convert return value to an int.
    - use `enum.IntEnum`
- Break code down to functions

Had help from [RealPython.com](https://realpython.com/python-rock-paper-scissors/)