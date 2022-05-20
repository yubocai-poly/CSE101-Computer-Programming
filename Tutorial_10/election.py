#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:55:32 2021

@author: Yubo Cai
"""


class Vote:
    """A single vote object.
    
    Data attributes:
    - preference_list: a list of the preferred parties for this voter,
      in descending order of preference.
    """
    def __init__(self, preference_list):
        self.preference_list = preference_list

    def __str__(self):
        if self.preference_list == []:
            return 'Blank'
        else:
            return ' > '.join(self.preference_list)

    def __repr__(self):
        return 'Vote({})'.format(self.preference_list)

    def first_preference(self):
        if len(self.preference_list) == 0:
            return None
        else:
            return self.preference_list[0]

    def preference(self, names):
        """Return the item in names that occurs first in the preference list,
        or None if no item in names appears.
        """
        for pref in self.preference_list:
            if pref in names:
                return pref
        else:
            return None


class Election:
    """A basic election class.
    
    Data attributes:
    - parties: a list of party names
    - blank: a list of blank votes
    - piles: a dictionary with party names for keys
      and lists of votes (allocated to the parties) for values
    """
    def __init__(self, parties):
        self.parties = parties
        self.blank = []
        self.piles = {name: [] for name in self.parties}
        self.dead = []

    def add_vote(self, vote):
        """Append the vote to the corresponding pile."""
        party = vote.first_preference()
        if party in self.piles:
            self.piles[party].append(vote)
        elif party not in self.piles:
            self.blank.append(vote)

    def status(self):
        """Return the current status of the election:
        a dictionary mapping each of the party names in the piles
        to the number of votes in their pile.
        """
        return {party: len(votes) for (party, votes) in self.piles.items()}

    def add_votes_from_file(self, filename):
        """
        Convert each line of the file into a Vote,
        and append each of the votes to the correct pile.
        """
        with open(filename, 'r') as readfile:
            for line in readfile:
                first_vote = line.split()
                vote1 = Vote(first_vote)
                self.add_vote(vote1)

    def first_past_the_post_winner(self):
        """Return the winner of this election under
        the first-past-the-post system, or None if
        the election is tied.
        """
        winner = None
        num_high = 0
        for (party, num) in self.status().items():
            if num > num_high:
                num_high = num
                winner = party
            elif num == num_high:
                winner = None
        return winner

    def weighted_status(self):
        """Returns a dictionary with keys being the parties
        and values being the number of points (counted using
        the weighted scheme) that the party got.
        """
        weighted_piles = {party: 0 for party in self.piles.keys()}
        for votes in self.piles.values():
            for vote in votes:
                i = 5
                for party in vote.preference_list:
                    weighted_piles[party] += i
                    i -= 1

        return weighted_piles

    def weighted_winner(self):
        """
        Return the winner of this election under
        the weighted voting scheme.
        """
        winner = None
        vote = 0
        for (party, num_high) in self.weighted_status().items():
            if num_high > vote:
                winner = party
                vote = num_high
            elif num_high == vote:
                winner = None
                vote = num_high
        if winner == None:
            winner_rank = sorted(self.weighted_status().keys())
            winner = winner_rank[0]

        return winner

    def eliminate(self, party):
        """Remove the given party from piles, and redistribute its 
        votes among the parties not yet eliminated, according to 
        their preferences.  If all preferences have been eliminated, 
        then add the vote to the dead list.
        """
        votes = self.piles[party]
        del self.piles[party]
        for sel in votes:
            if sel.preference(self.piles) is None:
                self.dead.append(sel)
            elif sel.preference(self.piles) is not None:
                self.piles[sel.preference(self.piles)].append(sel)

    def round_loser(self):
        """Return the name of the party to be eliminated in the next round
        of a preferential election."""
        party_first = 0
        loser_first = 0
        (loser, lowest) = (None, None)
        for (party, total) in self.status().items():
            if loser is None:  
                loser = party
                lowest = total
            elif total < lowest:
                loser = party
                lowest = total
            elif total == lowest:
                for vote in self.piles[party]:
                    if vote.first_preference() == party:
                        party_first += 1
                for vote in self.piles[loser]:
                    if vote.first_preference() == loser:
                        loser_first += 1
            if party_first < loser_first:
                loser = party
                lowest = total
            elif party_first == loser_first:
                if party < loser:
                    loser = party
                    lowest = total

        return loser

    def preferential_winner(self):
        """Run a preferential election based on the current piles of votes,
        and return the winning party.
        """
        while len(self.piles) > 1:
            self.eliminate(self.round_loser())
        list1 = self.piles.popitem()
        return list1[0]
