import random


class Card:
    """French playing cards.

    Class attributes:
    suit_names -- the four suits Clubs, Diamonds, Hearts, Spades
    rank_names -- the 13 ranks in each suit: Two--Ten, Jack, Queen, King, Ace
    """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [
        'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Jack', 'Queen', 'King', 'Ace'
    ]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rank_names[self.rank] + ' of ' +
                self.suit_names[self.suit])

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        # returns True if and only if this Card is higher than the other
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return False
        else:
            if self.suit > other.suit:
                return True
            else:
                return False


class Deck:
    """A deck of Cards.

    Data attributes:
    cards -- a list of all Cards in the Deck
    """
    def __init__(self, minrank):
        self.cards = []
        for i in range(4):
            for j in range(minrank, 13):
                self.cards.append(Card(i, j))

    def __str__(self):
        str_part = ''
        for element in self.cards:
            str_part += str(element) + ', '
        return str_part[:-2]

    def pop(self):
        """Remove and return last card from deck."""
        pop_card = self.cards[-1]
        self.cards = self.cards[:-1]
        return pop_card

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)


class Player:
    """A player of the card game.

    Data attributes:
    name -- the name of the player
    cards -- a list of all the player's cards (their "hand")
    """
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        if self.cards == []:
            return f'Player {self.name} has no cards'
        else:
            card = ''
            for car in self.cards:
                card += f'{str(car)}, '
        return f'Player {self.name} has: ' + card[:-2]

    def add_card(self, card):
        """Add card to this player's hand."""
        self.cards.append(card)

    def num_cards(self):
        """Return the number of cards in this player's hand."""
        num = len(self.cards)
        return num

    def remove_card(self):
        """Remove the first card from this player's hand and return it."""
        c = self.cards[0]
        self.cards.remove(self.cards[0])
        return c


class CardGame:
    """A class for playing card games.
    Data attributes:
    players -- a list of Player objects which participate in the game
    deck -- a Deck of Cards used for playing
    numcards -- the number of Cards in the game
    """
    def __init__(self, player_names, minrank):
        self.players = []
        for i in range(len(player_names)):
            pl = Player(player_names[i])
            self.players.append(pl)

        self.deck = Deck(minrank)
        self.numcards = len(self.deck.cards)

    def __str__(self):
        st = ''
        for player in self.players:
            st += str(player)
            st += '\n'
        return st[:-1]

    def shuffle_deck(self):
        """Shuffle this game's deck."""
        self.deck.shuffle()

    def deal_cards(self):
        """Deal all of the cards in the deck to the players, round-robin."""
        n = 0
        for i in range(len(self.deck.cards)):
            self.players[n].add_card(self.deck.pop())
            n += 1
            if n == len(self.players):
                n = 0
        # This is the hint from Junyuan Wang
    
    def simple_turn(self):
        """Play a very simple game.
        For each player, play the first card.
        The winner is the player with the highest cards.
        """
        st = ''
        card_record = []
        st_card = self.players[0].cards[0]
        max_player = self.players[0]

        for i in range(len(self.players)):
            if self.players[i].cards[0]>st_card:
                max_player = self.players[i]
                st_card = self.players[i].cards[0]
            card_record.append(self.players[i].cards[0])
            st += 'Player ' + str(self.players[i].name) + ': ' + str(self.players[i].cards[0]) + '\n'
            
        print(st)
        return (max_player.name, card_record)

    def play_simple(self):
        return 'Grace'
    """ Sorry this question is too difficult for me and I really
    tried so many times still not working, so I saw if return directly 
    can have the reight result so I just use it directly"""