# Connect 4 with AI <br>
## Overview <br>
This project implements a classic Connect 4 game in Python, featuring a graphical user interface provided by Pygame and an AI opponent powered by a minimax algorithm with alpha-beta pruning and iterative deepening. The AI's strategy is based on evaluating the game board to make intelligent moves against the player.  <br>

## Installation <br>
### Prerequisites  <br>
Python 3.x  <br>

Pip (Python package installer) <br>

### Dependencies 
Install the required Python packages using pip:

```
pip install pygame numpy
```
Running the Game  <br> 
To start the game, navigate to the project directory and run the following command in your terminal:  <br>

bash  <br>
Copy code  
```
python connect4.py  
```

Make sure to replace connect4.py with comparison and my_connect4_ai to use those instead.  <br>

## Game Rules  <br>
The game is played on a vertical board consisting of 6 rows and 7 columns.  <br>
Two players take turns dropping colored discs into the columns of the board.  <br>
The first player to align four discs vertically, horizontally, or diagonally wins the game.  <br>
If all columns are filled and no player has achieved a line of four, the game is a draw.  <br>
## Features  <br>
Graphical User Interface: Utilizes Pygame for rendering the game board and handling user interactions.
AI Opponent: Employs a minimax algorithm with enhancements such as alpha-beta pruning for efficiency and iterative deepening for improved decision-making.  <br>
Dynamic Board Evaluation: The board is dynamically evaluated after each move to update the game state and determine the winner.  <br>
## Contributions  <br>
Contributions to the project are welcome. Please ensure that you submit a pull request for review before merging your changes.  <br>

## License  <br>
This project is open-sourced<br>

## Credits  <br>
Base code adapted from Keith Galli's Connect 4 repository.  <br>
Project maintained and extended by Tung Nguyen.  <br>
