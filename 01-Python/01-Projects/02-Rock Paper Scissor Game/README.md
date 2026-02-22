# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock Paper Scissors game in Python.

## Description

This is a text-based game where you play Rock Paper Scissors against the computer. The computer makes random choices, and the winner is determined based on the traditional rules of the game.

## Game Rules

- Rock vs Paper → Paper wins
- Rock vs Scissors → Rock wins
- Paper vs Scissors → Scissors wins

## Requirements

- Python 3.x
- No external libraries required (uses built-in `random` module)

## How to Run

1. Make sure you have Python installed on your system
2. Save the game code as `rock_paper_scissors.py`
3. Open a terminal/command prompt
4. Navigate to the directory containing the file
5. Run the command:
   ```bash
   python rock_paper_scissors.py
   ```

## How to Play

1. When prompted, enter your choice:
   - Enter `1` for Rock
   - Enter `2` for Paper
   - Enter `3` for Scissors

2. The computer will randomly select its choice

3. The winner will be displayed based on the game rules

4. After each round, you'll be asked if you want to play again:
   - Enter `Y` to continue playing
   - Enter `N` to exit the game

## Example Gameplay

```
Enter your choice 
 1 - Rock 
 2 - Paper 
 3 - Scissors 

Enter your choice: 1
User choice is: Rock
Now it's Computer's Turn...
Computer choice is: Scissors
Rock vs Scissors
<== User wins! ==>
Do you want to play again? (Y/N)
```

## Features

- Input validation to ensure valid choices
- Continuous play option
- Clear display of game results
- Random computer opponent

## License

Free to use and modify.