#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class Card:
    """French playing cards.

    Class attributes:
    suit_names -- the four suits Clubs, Diamonds, Hearts, Spades
    rank_names -- the 13 ranks in each suit: Two--Ten, Jack, Queen, King, Ace
    """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                  'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']            

    def __init__(self, suit, rank):      
        self.suit = suit
        self.rank = rank       

    def __str__(self):  # Readable string representation
        return (self.rank_names[self.rank] + ' of ' + self.suit_names[self.suit])

    def __eq__(self, other):
        """The __eq__() method provides a deep equality check for cards.
        Returns True if, and only if, two cards have the same rank 
        and the same suit.
        """
        return ((self.suit, self.rank) == (other.suit, other.rank))
        
    def matching_card(self):
        """Return the card which matches self.
        For example, find_match(Card(0,4)) == Card(3,4)
        """  
        return Card(3 - self.suit, self.rank)

class Deck:
    """A deck of Cards.

    Data attributes:
    cards -- a list of all Cards in the Deck
    """

    def __init__(self, minrank = 0):
        """__init__() method should take 
        an extra parameter minrank, an integer with a default
        value of 0.
        #####################################################
        We will use minrank to create decks of cards which do 
        not contain some of the smaller cards. Thus, Deck(n) should 
        create a deck which does not contain the first n ranks.
        """
        self.cards = [] 
        for suit in range(len(Card.suit_names)): 
            for rank in range(minrank,len(Card.rank_names)):
                if Card(suit,rank) == Card(0,10):
                    continue
                self.cards.append(Card(suit,rank))  
        
    def __str__(self):
        parts = [str(card) for card in self.cards]
        for card in self.cards:
            parts.append(str(card))
        return ', '.join(res)
        # alternatively:
        # return ', '.join([str(card) for card in self.cards])
        
    def pop(self):
        """Remove and return last card from deck."""
        return self.cards.pop()
        
    def shuffle(self):
        """Shuffle the deck."""    
        random.shuffle(self.cards)
                       
class Player:
    """A player of the card game.

    Data attributes:
    name -- the name of the player (default '')
    cards -- a list of all the player's cards
    """ 
    def __init__(self,name=''):
        self.name = name
        self.cards = []
        
    def __str__(self):
        """A string containing the player's cards, or "has no cards"
        if the player has no cards. For example, print(Player('Adam'))
        should return "Player Adam has no cards" or 
        "Player Adam has: Four of Spades, Two of Hearts"
        """
        if self.cards == []:
            return 'Player ' + self.name + ' has no cards'
        res = []
        s =  'Player ' + self.name + ' has: ' 
        for car in self.cards:
            res.append(str(car))
        return s + ', '.join(res)
        ## alternatively, using list comprehensions:
        # res = 'Player ' + self.name + ' has'
        # if len(self.cards) == 0:
        #     return res + ' no cards'
        # res += ': '
        # res += ', '.join([str(card) for card in cards])
        # return res
        
    def add_card(self, card):
        """Add card to hand."""
        self.cards.append(card)
        
    def num_cards(self):
        """Return number of cards in hand."""
        return len(self.cards)
        
    def remove_card(self, i):
        """Removes and returns the ith card from the player’s hand."""
        return self.cards.pop(i)

    def remove_matches(self):
        """Remove all pairs of matching cards."""
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = card.matching_card()
            if match in self.cards:
                print('Player {}: {} matches {}'.format(self.name, card, match))
                self.cards.remove(card)
                self.cards.remove(match)
                count = count + 1
        return count

class CardGame:
    """A class for playing card games.

    Data attributes:
    players -- a list of Player objects which participate in the game
    deck -- a Deck of Cards used for playing
    numcards -- number of Cards in the game
    """      

    def __init__(self,players,minrank = 0):
        ## alternative using list comprehension:
        # self.players = [Player(p) for p in players]
        # self.deck = Deck(minrank)
        # self.numcards = len(self.deck.cards)
        lis = []
        for p in players:
            lis.append(Player(p))
        self.players = lis
        self.deck = Deck(minrank)
        self.numcards = len(self.deck.cards)

    def __str__(self):
        ## much simpler alternative using list comprehension:
        # return '\n'.join([str(p) for p in self.players])
        s = ''
        for p in self.players:
            s += str(p) +'\n'
        return s[:-1]
        
    def shuffle_deck(self):
        self.deck.shuffle() 

    def deal_cards(self):            
        for i in range(self.numcards):
            for p in self.players:
                if len(self.deck.cards) == 0:
                    continue
                card = self.deck.pop()
                Player.add_card(p, card)
 

    def simple_play(self):
        """Play a simple matching game.
        For each player, remove all matching pairs.
        Winners are the players with the most matches.
        """
        ## simpler: counts = [p.remove_matches() for p in self.players]
        counts = []
        for p in self.players:
            counts.append(p.remove_matches())
        m = max(counts)

        winner_names = []
        for i in range(len(counts)):
            if counts[i] == m:
                winner_names.append(self.players[i].name)

        if len(winner_names) == 1:
            mesg = 'The winner is ' + winner_names[0]
        else:
            mesg = 'The winners are '
            mesg += ' and '.join(winner_names)
        print(mesg)

    def find_neighbor(self, p):
        """Find neighbor of player p, to pick a card from."""
        num_hands = len(self.players)
        for next in range(1,num_hands):
            neighbor_index = (p + next) % num_hands
            if self.players[neighbor_index].cards:
                return neighbor_index
            
    def play_one_turn(self, p):
        """Play one Svarteper turn:
        If player p has any cards, pick a random card from neighbor
        and afterwards remove matches.
        Returns number of matching pairs removed
        """
        player = self.players[p]
        neighbor = self.players[self.find_neighbor(p)]
        if not player.cards:
            return 
        picked_index = random.randint(0,len(neighbor.cards))
        picked_card = neighbor.cards.pop(picked_index)
        print('Player {}: takes {} from {}'.format(player, picked_card, neighbour))
        player.add_card(picked_card)
        count = player.remove_matches()
        return count