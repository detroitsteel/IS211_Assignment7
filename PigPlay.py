#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IGood ol family fun game of pig"""

import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(len(self.items),item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def pigGame(numply):
    """pigGame Function - Play the game pig with unlimited players.
    The rules of Pig are simple.
    The game features at least two players, with the goal of reaching 100 points
    first. Each turn, a player repeatedly rolls a die until either a 1 is rolled
    or the player holds and scores the sum of the rolls (i.e. the turn total).
    At any time during a player's turn, the player is faced with two decisions:
    roll ­ If the player rolls a 1: the player scores nothing and it becomes the
    opponent's turn. if the player rolls 2 ­ 6: the number is added to the
    player's turn total and the player's turn continues. hold ­ The turn total
    is added to the player's score and it becomes the opponent's turn.
    Args:
        numply (int): The number of players who will play the game
    Output: Game play according to the rules
    Example:
        >>> pigGame(2)
        >>>Player 1 current turn score is 0.
            1 roll(s) of the die returns 5.
            Roll again type R or to hold type H:h
            Next Player
            Player 2 turn.
            .....
            Player 1 turn.
            Player 1 score is currently 99.

            Player 1 current turn score is 0.
            26 roll(s) of the die returns 6.
            Roll again type R or to hold type H:h
            Player 1 wins
    """
    dieroll = 0
    rollturn = 1
    turnpoints = 0
    a_waiting_lst = []
    ply_queue = Queue()
    ply_dict = {}
    gameOn = 1
    plyOn = 1
    for ply in range(numply):
        ply_queue.enqueue(ply + 1)
        ply_dict.update({ply + 1: (turnpoints, dieroll)})
    while gameOn:
        plyturn = ply_queue.items[0]
        turnpoints = ply_dict[plyturn][1]
        rollturn = (ply_dict[plyturn][0]) + 1
        curturnpoints = 0
        plyOn = 1
        dieroll = random.randint(1,6)
        print ("Player %i turn.\nPlayer %i score is currently %i.\n"
               %(plyturn, plyturn, turnpoints))
        while plyOn:
            if dieroll == 1:
                print '\n!!OOOPS, you rolled a 1. Next Players turn!!\n'
                ply_queue.dequeue()
                ply_queue.enqueue(plyturn)
                plyOn = 0
                break
            print ("Player %i current turn score is %i.\n"
                   "%i roll(s) of the die returns %i."
                   %(plyturn, curturnpoints, rollturn, dieroll))
            plydecide = (raw_input("Roll again type R or to hold type H:\n"))
            plydecide = plydecide.upper()
            curturnpoints = curturnpoints + dieroll
            if plydecide == 'R':
                dieroll = random.randint(1,6)
                rollturn += 1
            elif plydecide == 'H':
                turnpoints = turnpoints + curturnpoints
                if turnpoints >= 100:
                    print "\n\nPlayer %i wins!!!!!" %plyturn
                    gameOn = 0
                    return
                print 'Next Player'
                ply_dict.update({plyturn: (rollturn, turnpoints)})
                ply_queue.dequeue()
                ply_queue.enqueue(plyturn)
                plyOn = 0
            else:
                print 'Invalid Entry, try again'
                break
