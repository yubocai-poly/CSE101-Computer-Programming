#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:47:26 2021

@author: apple
"""
import random

def play_hilo(x,n):
    """A simple guessing game.
    The player has to guess the target value x in at most n attempts.
    """
    
    print('Guess what number I am thinking of?')
    
    while n > 0:
        print('You have', n , 'turns left')
        guess1 = int(input('Guess:'))
        if guess1 == x:
            print('Congratulations!')
            return
        if guess1 > x:
            print('Higher')
        if guess1 < x:
            print('lower')
        n -= 1
    if n == 0:
        print('You lose!')
        
def play_random_hilo(lower,upper,n):
    """Play the hilo game with the target value x chosen 
    randomly from the interval [lower,upper].
    """
    
    x = random.randint(lower,upper)
    play_hilo(x,n)
    
def warmer_or_colder(lower,upper,n):
    
    x = random.randint(lower,upper)
   
    print('Guess what number I am thinking of?')
    
    old_guess = 0

    while n > 0:
        print('You have', n , 'turns left')
        guess1 = int(input('Guess:'))
        if guess1 == x:
            print('Congratulations!')
            return
        if abs(guess1 - x) < abs(old_guess - x ):
            print('getting warmer')
        if abs(guess1 - x) > abs(old_guess - x ):
            print('getting colder')
        if abs(guess1 - x) == abs(old_guess - x ):
            print('getting nowhere')
        old_guess = guess1
        n = n - 1
    
    if n == 0:
        print('You lose!')
    
    
        
