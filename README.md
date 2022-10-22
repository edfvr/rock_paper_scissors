# Rock Paper Scissors

## Pseudocode
1. take user input and store in a variable
2. Make a list of moves. i.e `["rock", "paper", "scissors"]`
3. Use `random.choice()` on `cpu_move` so that the computer selects moves randomly.
    - import `random` to be able to use `random.choice()`
4. print `user_move` and `cpu_move` to update user
5. Set conditions for winning *(rock smashes scissors, paper covers rock, scissors cuts paper)*
    - if player = cpu, it's a tie
    - if player = rock and cpu = scissors, player wins
        else if cpu = paper, cpu wins
    - if player = paper and cpu = rock, player wins
        else if cpu = scissors, cpu wins
    - if player = scissors and cpu = paper, player wins
        else if cpu = rock, cpu wins