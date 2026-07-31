"""
1-The game is played between two players who take turns one after another.
2- On each turn, a player can call 1 to 3 numbers.
3- The numbers must be consecutive (for example, 5 6 7) skipping numbers leads to disqualification.
4- The counting always starts from 1 and continues upward.
5- The one who calls 21, loses the game.
"""
# import asyncio
from __init__ import player_function, computer_function
import random
turn = random.randint(1, 2)
#print(turn)
player_turn = False
computer_turn = False

game_loop = True
while game_loop:
    if turn == 1:
        player_turn = True
    else:
        computer_turn = True
    if player_turn == True:
        player_function()
    else:
        computer_function()
    player_turn = False
    computer_turn = False
    game_loop = False