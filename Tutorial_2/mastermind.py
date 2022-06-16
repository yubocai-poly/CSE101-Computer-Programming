#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:01:01 2021

@author: Yubo Cai
"""

# Exercise 1
import random
COLORS = ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']

def input_color(color):
    """Return True if the given input color can be found in COLORS
       Use a for-loop to iterate over the list of COLORS.
    """
    for colors in COLORS:
        if color == colors:
            return True
    return False

# Exercise 2
def create_code():
    """Return 4-element list of strings randomly chosen from
    COLORS with repetition.
    """
    s = []
    for i in range(4):
        colors = random.choice(COLORS)
        s.append(colors)
    return s

# Exercise 3
def black_pins(guess, code):
    """guess, code: 4-element lists of strings from COLORS
    Returns the number of black pins, determined by the standard
    Mastermind rules, plus guess and code lists with matching
    pins removed"""
    
    blackpins = 0
    new_guess = []
    new_code = []
    for i in range(4): 
        if guess[i] == code[i]: 
            blackpins += 1
    return blackpins

# Exercise 4
def score_guess(guess, code):
    """guess, code: 4-element lists of strings
    Return (black, white) where
    black is the number of black pins (exact matches), and
    white is the number of white pins (correct colors in wrong places)
    """
    new_guess = []
    new_code = []
    for i in range(4): 
        if guess[i] != code[i]:
            new_guess.append(guess[i])
            new_code.append(code[i])
            
    black = black_pins(guess, code)
    white = 0
    
    for i in range(len(new_guess)):
        if new_guess[i] in new_code:
            white += 1
            new_code.remove(new_guess[i])

    return(black, white)

# Exercise 5
def str_with_suffix(n):
    if n % 10 == 1 and n % 100 != 11:
        suffix = 'st'
    elif n % 10 == 2 and n % 100 != 12:
        suffix = 'nd'
    elif n % 10 == 3 and n % 100 != 13:
        suffix = 'rd'
    else:
        suffix = 'th'
    return str(n) + suffix
    
def input_guess():
    """Input four colors from COLORS and return as list.
    """
    n = 1
    enter_guess = []
    print('Enter your guess:')
    
    for i in range(1000):
        if len(enter_guess) >= 4:
            break
        l = input(str_with_suffix(n) + 'pin:')
        if l in COLORS:
            n += 1
            enter_guess.append(l)
        else:
            print("Please input a color from the list ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']")
    return enter_guess

# Exercise 6
def one_round(code):
    """Input guess, score guess, print result, and return True iff
    user has won.
    """
    
    guess = input_guess()
    black , white = score_guess(guess, code)
    print('Score:', black, 'black,', white, 'white')
    if black == 4:
        return True
    else:
        return False
    
# Exercise 7
def play_mastermind(code):
    """Generate random Mastermind code and let user guess it in rounds
    """
    r = 1
    for i in range(10000):
        print('Round ' + str(r))
        if one_round(code) is False:
            r += 1
        else:
            print('You Win!')
            break


