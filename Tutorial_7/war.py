#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSE101 - Computer Programming 
Tutorial 7 - Naive War (card game)
Created on Wed Sep 29 21:01:01 2021

@author: Yubo Cai
"""

import random


# Exercise 1 - A Class for Playing Cards
class Card:
    """
    French playing cards.

    Class attributes:
    suit_names -- the four suits Clubs, Diamonds, Hearts, Spades
    rank_names -- the 13 ranks in each suit: Two--Ten, Jack, Queen, King, Ace

    Data attributes:
    suit, rank -- the Card's suit and rank, as indices into the lists above
    """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [
        'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Jack', 'Queen', 'King', 'Ace'
    ]

    def __init__(self, suit, rank):
        self.suit = suit  # from 0 to 3
        self.rank = rank  # from 0 to 12

    def __str__(self):
        """
        Return a string representation of the card.
        """
        return f'{self.rank_names[self.rank]} of {self.suit_names[self.suit]}'

# Interlude: Some Cards Are More Equal Than Others

    def __eq__(self, other):
        """
        Return True if self and other have the same rank and suit.
        """
        return self.suit == other.suit and self.rank == other.rank

    def __gt__(self, other):
        # returns True if and only if this Card is higher than the other
        if self.rank > other.rank:
            return True
        elif self.rank == other.rank:
            return self.suit > other.suit
        else:
            return False


# Exercise 2 - A Class for Decks of Cards
class Deck:
    """
    A deck of Cards.

    Data attributes:
    cards -- a list of all Cards in the Deck
    """

    def __init__(self, minrank):
        self.cards = []
        for suit in range(4):
            for rank in range(minrank, 13):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        """
        Return a string representation of the Deck.
        """
        return ', '.join(str(card) for card in self.cards)

# Exercise 3 - More about Decks

    def pop(self):
        """Remove and return last card from deck."""
        pop_card = self.cards[-1]
        self.cards = self.cards[:-1]
        return pop_card

    def shuffle(self):
        """Shuffle the deck."""
        return random.shuffle(self.cards)


# Exercise 4 - A Class for Players
class Player:
    """
    A player of the card game.

    Data attributes:
    name -- the name of the player
    cards -- a list of all the player's cards (their "hand")
    """

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        """
        Return a string representation of the Player.
        """
        if self.cards == []:
            return f'Player {self.name} has no cards'
        else:
            cards = ''
            for card in self.cards:
                cards += f'{str(card)}, '
            return f'Player {self.name} has: {cards[:-2]}'

# Exercise 5 - Players Playing

    def add_card(self, card):
        """Add card to this player's hand."""
        self.cards.append(card)

    def num_cards(self):
        """Return the number of cards in this player's hand."""
        return len(self.cards)

    def remove_card(self):
        """Remove the first card from this player's hand and return it."""
        return self.cards.pop(0)


# Exercise 6 - A Class for Card Games
class CardGame:
    """
    A class for playing card games.

    Data attributes:
    players -- a list of Player objects which participate in the game
    deck -- a Deck of Cards used for playing
    numcards -- the number of Cards in the game
    """

    def __init__(self, player_names, minrank):
        self.deck = Deck(minrank)
        self.numcards = len(self.deck.cards)
        self.players = []
        for name in player_names:
            self.players.append(Player(name))

    def __str__(self):
        """
        Return a string representation of the CardGame.
        """
        string = ''
        for name in self.players:
            string += f'{name}\n'
        return string[:-1]

# Exercise 7 - Dealing Cards

    def shuffle_deck(self):
        """Shuffle this game's deck."""
        self.deck.shuffle()

    def deal_cards(self):
        """
        这道题用双指针的方法解决
        Deal all of the cards in the deck to the players, round-robin.
        """
        n = 0
        for i in range(self.numcards):
            self.players[n].add_card(self.deck.pop())
            n += 1
            if n == len(self.players):
                n = 0


# Exercise 8 - Playing “Find the highest”

    def simple_turn(self):
        """
        Play a very simple game.
        For each player, play the first card.
        The winner is the player with the highest cards.
        """
        st = ''
        record = []
        st_card = self.players[0].cards[0]
        winner = self.players[0]

        for i in range(len(self.players)):
            if self.players[i].cards:
                if self.players[i].cards[0] > st_card:
                    st_card = self.players[i].cards[0]
                    winner = self.players[i]
                record.append(self.players[i].cards[0])
                st += f'Player {str(self.players[i].name)}: {str(self.players[i].cards[0])}\n'

        print(st)
        return winner.name, record 


# Exercise 9 - Playing this simple game

    def play_simple(self):
        """
        这个游戏存在一些逻辑硬伤, 在发牌阶段，会从牌堆的最后一张牌开始发牌, 并且牌堆的顺序是完全有序的, 因此第一个得到牌的玩家的点数一定比其他人大,
        所以最后的赢家也相对应一定是第一个玩家, 所以最后甚至可以直接返回Grace
        """
        num = self.numcards // len(self.players)
        for i in range(num):
            winner, record = self.simple_turn()
            for player in self.players:
                if player.name != winner and player.cards:
                    player.remove_card()
                elif player.name == winner:
                    player.remove_card()
                    for card in record:
                        player.add_card(card)
            winner = ''
            record = []
        
        for player in self.players:
            if player.num_cards() == self.numcards:
                return player.name

        
        
        
        