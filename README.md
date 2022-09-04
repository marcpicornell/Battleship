# Super Battleship

## How to play

## Features

## Data Model
I have decied to use 4 classes for the implementation of the game.
* Player: handle humand and computer user
* Board: handle the board
* Boat: handle boats
* Game: handle the game logic

Game will inherit the others.

### Data Model Details

#### Player:
One instance for human
One instance for computer

#### Board:
One instance of the grid for human player
One instance of the grid for computer player

#### Boat:

#### Game:



## Implementation
I am using the python module termcolor to make the terminal a bit more colorful.
Future improvement could use curses to build menu and a nice board. (see https://docs.python.org/3/howto/curses.html)

### Existing Features

The game use the original battleship board size of 10 x 10.
* Value from 1 to 10
* Value from A to J

Boat size is currently limited to 1x1



### Future Features
Battleship will use the new boat definition:
* Carrier size 5
* Battleship size 4
* Destroyer size 3
* Submarine size 3
* Patrol Boat size 2

Allow player to define the size of the grid up to 40 x 40
Allow boats to be position if player is human
Allow larger ship following the list of boat definition above

## Testing

### Bugs
### Remaining Bugs
### Validator Testing

## Deployment

## Credits

* Code Institue for this program and supporting materials
* Wikipedia for providing the details of the game. I haven't plaid this games for decades :-(
https://en.wikipedia.org/wiki/Battleship_(game)
* Termcolor: color in the terminal
https://pypi.org/project/termcolor/
* Screen CLEAR taken from the tuto
https://www.tutorialspoint.com/how-to-clear-python-shell#:~:text=The%20commands%20used%20to%20clear,shell%20are%20cls%20and%20clear.
