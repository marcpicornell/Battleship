'''

.______        ___   .___________.___________. __       _______     _______. __    __   __  .______   
|   _  \      /   \  |           |           ||  |     |   ____|   /       ||  |  |  | |  | |   _  \  
|  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__     |   (----`|  |__|  | |  | |  |_)  | 
|   _  <    /  /_\  \    |  |        |  |     |  |     |   __|     \   \    |   __   | |  | |   ___/  
|  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____.----)   |   |  |  |  | |  | |  |      
|______/  /__/     \__\  |__|        |__|     |_______||_______|_______/    |__|  |__| |__| | _|      
                                                                                                      
'''

import os                                   # required for the clear function ()
from termcolor import colored, cprint       # required for termcolor support
from random import randint                  # required to generate random numbers

'''
Definition of constant for the project.
SIZE: 10 -> grid size (will then be 10x10)
NUMBER_OF_BOATS: 5 -> number of boat per board
ROBOTS: contain the list of name that the computer will use to take a pseudonyme
'''

SIZE = 10
NUMBER_OF_BOATS = 5
ROBOTS = ("R2-D2", "C-3PO", "Gort", "T800", "Number 6")

'''
    Definition of global variables, ... if needed.
    Like in C, I believe that global variables should be avoided when possible.
'''

scores = {
    "human_player": 0,          # hold human score
    "computer_player": 0        # hold computer score
    }

class Player:
    '''
    '''
    pass

class Board:
    '''
    '''
    pass

class Boat:
    '''
    '''
    pass

class Game:
    '''
    '''
    pass

def clear():
    '''
    Clean the screen before printing anything in the terminal
    '''
    os.system('clear')


def main():
    '''
    First fonction to be run in Python
    '''
    clear()

main()