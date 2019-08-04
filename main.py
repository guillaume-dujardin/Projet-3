#!/usr/bin/python3

from Game import Game

def launching(): # function to start the game
    first_game = Game()
    first_game.play()
                   
if __name__ == "__main__" :
    launching() # call the function to launch the program
