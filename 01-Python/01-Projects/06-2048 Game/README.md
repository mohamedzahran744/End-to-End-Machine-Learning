# 2048 Game

A Python implementation of the popular 2048 puzzle game with command-line interface.

## Description

This is a console-based version of the classic 2048 game where you combine numbered tiles to reach the goal of creating a tile with the number 2048. The game uses keyboard controls to slide tiles in four directions, merging tiles with the same number.

## Game Rules

- The game is played on a 4×4 grid
- Use keyboard controls to slide all tiles in one direction (up, down, left, or right)
- When two tiles with the same number touch, they merge into one tile with double the value
- After each move, a new tile (with value 2) appears in a random empty spot
- The goal is to create a tile with the value 2048
- The game ends when no more moves are possible

## Features

- **4×4 Grid Gameplay**: Classic 2048 game board
- **Merge Mechanics**: Combine tiles with the same value
- **Random Tile Generation**: New tiles appear after each valid move
- **Win/Loss Detection**: Automatic game state checking
- **Keyboard Controls**: Simple WASD controls for movement

## Requirements

- Python 3.x
- No external libraries required (uses only standard Python modules)

## Installation

1. Ensure Python 3.x is installed on your system
2. Download the game files:
   - `Game.py` (contains all game logic)
   - Main game file (for running the game)
3. Keep both files in the same directory

## Controls

```
W or w : Move Up
S or s : Move Down
A or a : Move Left
D or d : Move Right
```

## How to Play

1. Run the main game file
2. A 4×4 grid will appear with initial tiles
3. Use WASD keys to move tiles in the desired direction
4. Tiles with the same number will merge when they collide
5. Try to reach 2048 to win!
6. The game ends when the board is full and no more moves are possible

## Game States

- **GAME NOT OVER**: You can still make moves
- **WON**: You've successfully created a 2048 tile
- **LOST**: The board is full and no valid moves remain

## Code Structure

### Main Functions

#### Game Initialization
- `start_game()`: Initializes a new 4×4 grid and adds the first tile

#### Core Game Logic
- `add_new_2(mat)`: Adds a new '2' tile to a random empty cell
- `get_current_state(mat)`: Checks if the game is won, lost, or still in progress
- `findEmpty(mat)`: Locates empty cells in the grid

#### Movement Functions
- `move_left(grid)`: Slides and merges tiles to the left
- `move_right(grid)`: Slides and merges tiles to the right
- `move_up(grid)`: Slides and merges tiles upward
- `move_down(grid)`: Slides and merges tiles downward

#### Helper Functions
- `compress(mat)`: Shifts all non-zero tiles to remove gaps
- `merge(mat)`: Combines adjacent tiles with the same value
- `reverse(mat)`: Reverses each row of the matrix
- `transpose(mat)`: Transposes the matrix (swaps rows and columns)

## Algorithm Overview

Each move follows this sequence:

1. **Compress**: Remove gaps between tiles
2. **Merge**: Combine tiles with the same value
3. **Compress Again**: Remove gaps created by merging
4. **Add New Tile**: Place a '2' in a random empty cell

For different directions:
- **Left**: Direct compression and merging
- **Right**: Reverse → Move Left → Reverse
- **Up**: Transpose → Move Left → Transpose
- **Down**: Transpose → Move Right → Transpose

## Example Gameplay

```
Initial Grid:
[2][0][0][0]
[0][0][0][0]
[0][0][0][0]
[0][0][2][0]

After Move Left:
[2][0][0][0]
[0][0][0][0]
[2][0][0][0]
[2][0][0][0]

After Merge:
[2][0][0][0]
[0][0][0][0]
[2][0][0][0]
[4][0][0][2]  <- New tile added
```

## Tips for Playing

- Plan your moves ahead to avoid filling the board too quickly
- Try to keep your highest value tile in a corner
- Build tiles in one direction to create larger combinations
- Don't make random moves - each move should have a purpose

## Technical Details

- **Grid Size**: 4×4 matrix
- **Initial Tile Value**: 2
- **Win Condition**: Creating a 2048 tile
- **Tile Generation**: Random placement in empty cells
- **Move Validation**: Checks if the move changes the board state

## File Structure

```
Game.py           # Contains all game logic and algorithms
main.py           # Main game loop and user interface (separate file)
README.md         # This file
```

## Future Enhancements

Possible improvements for this game:
- Graphical user interface using Tkinter or Pygame
- Score tracking system
- Undo functionality
- Save/Load game state
- Different grid sizes (3×3, 5×5)
- Animation effects

## License

This is an educational project and is free to use and modify.

## Acknowledgments

Based on the original 2048 game created by Gabriele Cirulli.