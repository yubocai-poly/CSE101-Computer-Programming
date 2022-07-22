#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSE101 - Computer Programming 
Tutorial 6 - Digital Pets
Created on Wed Sep 29 21:01:01 2021

@author: Yubo Cai
"""


# Exercise 1 - A new pet is born
class Trobble:
    """
    Trobbles: simplified digital pets.

    Data Attributes:
    name -- the Trobble's name.
    sex -- 'male' or 'female'.
    age -- a non-negative integer
    health -- an integer between 0 (dead) and 10 (full health) inclusive
    hunger -- a non-negative integer (0 is not hungry)
    """

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.age = 0
        self.health = 10
        self.hunger = 0

# Exercise 2 -  Showing what we got

    def __str__(self):
        return f'{self.name}: {self.sex}, health {self.health}, hunger {self.hunger}, age {self.age}'

# Exercise 3 -  Growing older

    def next_turn(self):
        """
        End the turn for the instance and recompute the attribute values
        for the next turn.
        """
        if self.health > 0:
            self.age += 1
            self.hunger += self.age
            self.health -= self.hunger // 20
            if self.health < 0:
                self.health = 0

# Exercise 4 -  Caring for your Trobble

# Exercise 4a -  Feeding

    def feed(self):
        """
        Feed the Trobble instance to decrease the hunger by 25
        with a minimum value of 0.
        """
        self.hunger -= 25
        if self.hunger < 0:
            self.hunger = 0

# Exercise 4b -  Curing

    def cure(self):
        """
        Increase the health of the instance by 5 up to the maximum of 10.
        """
        self.health += 5
        if self.health > 10:
            self.health = 10

# Exercise 4c -  Having fun

    def have_fun(self):
        """
        Increase the health of the instance by 2 up to the maximum of 10 
	    and increase the hunger by 4.
        """
        self.health += 2
        self.hunger += 4
        if self.health > 10:
            self.health = 10

# Exercise 4d -  Checking

    def is_alive(self):
        """
        Return True if the health of the instance is positive,
        otherwise False.
        """
        if self.health > 0:
            return True
        else:
            return False


# Exercise 5 -  Playing with Trobbles
def get_name():
    return input('Please give your new Trobble a name: ')


def get_sex():
    sex = None
    while sex is None:
        prompt = 'Is your new Trobble male or female? Type "m" or "f" to choose: '
        choice = input(prompt)
        if choice == 'm':
            sex = 'male'
        elif choice == 'f':
            sex = 'female'
    return sex


def get_action(actions):
    while True:
        prompt = f"Type one of {', '.join(actions.keys())} to perform the action: "
        action_string = input(prompt)
        if action_string not in actions:
            print('Unknown action!')
        else:
            return actions[action_string]


# Exercise 5a - Play
def play():
    name = get_name()
    sex = get_sex()
    trobble = Trobble(name, sex)
    actions = {'feed': trobble.feed, 'cure': trobble.cure}
    while trobble.is_alive():
        print('You have one Trobble named ' + str(trobble))
        action = get_action(actions)
        action()
        trobble.next_turn()
    print(
        f'Unfortunately, your Trobble {trobble.name} has died at the age of {trobble.age}'
    )


# Exercise 6 - Be fruitful, and multiply
def mate(trobble1, trobble2, name_offspring):
    """
    Check if the given Trobbles can procreate and if so give back a new
    Trobble that has the sex of trobble1 and the name 'name_offspring'.
    Otherwise, return None.
    """
    if trobble1.age > 3 and trobble2.age > 3 and trobble1.sex != trobble2.sex and trobble1.health > 0 and trobble2.health > 0:
        return Trobble(name_offspring, trobble1.sex)
    else:
        return None
    
# Optional Exercise 7 - More Trobbles, more troubles
def get_sex2():
    sex = None
    while sex is None:
        prompt = 'Which sex you want your first Troblle to be? Type "m" or "f" to choose: '
        choice = input(prompt)
        if choice == 'm':
            sex = 'male'
        elif choice == 'f':
            sex = 'female'
    return sex

def multi_play():
    name1 = input('Please give your first Trobble a name: ')
    name2 = input('Please give your second Trobble a name: ')
    sex1 = get_sex2()
    if sex1 == 'female':
        sex2 = 'male'
    else:
        sex2 = 'female'
    trobble1 = Trobble(name1, sex1)
    trobble2 = Trobble(name2, sex2)
    while trobble1.is_alive() or trobble2.is_alive():
        index = input('Which one you want to have action, please enter 1 or 2: ')
        if index == 1:
            actions = {'feed': trobble1.feed, 'cure': trobble1.cure}
            if trobble1.is_alive():
                print('You have one Trobble named ' + str(trobble1))
                action = get_action(actions)
                action()
                trobble1.next_turn()
        if index == 2:
            actions = {'feed': trobble2.feed, 'cure': trobble1.cure}
            if trobble2.is_alive():
                print('You have one Trobble named ' + str(trobble2))
                action = get_action(actions)
                action()
                trobble2.next_turn()
    
    

