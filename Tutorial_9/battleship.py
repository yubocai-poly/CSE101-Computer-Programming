#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:01:31 2021

@author: Yubo Cai
"""

import random
# List of tuples: (name, length) where length is the number of positions of your ship
ship_types = [('Battleship', 4), ('Carrier', 5), ('Cruiser', 3),
              ('Destroyer', 2), ('Submarine', 3)]


class Ship:
    """A ship that can be placed on the grid."""
    def __repr__(self):
        return f"Ship('{self.name}', {self.positions})"

    def __str__(self):
        return f'{repr(self)} with hits {self.hits}'

    def __init__(self, name, positions):
        self.name = name
        self.positions = positions
        self.hits = set()

    def __eq__(self, other):
        if self.name == other.name and self.positions == other.positions and self.hits == other.hits:
            return True
        else:
            return False

    def is_afloat(self):
        if self.positions == self.hits:
            return False
        else:
            return True

    def take_shot(self, shot):
        """Check if the shot hits the ship. If so, remember the hit.
        Returns one of 'MISS', 'HIT', or 'DESTROYED'.
        """
        if shot in self.positions and shot not in self.hits:
            self.hits.add(shot)
            if self.hits == self.positions:
                return 'DESTROYED'
            else:
                return 'HIT'
        else:
            return 'MISS'


class Grid:
    """Encodes the grid on which the Ships are placed.
    Also remembers the shots fired that missed all of the Ships.
    """
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.ships = []
        self.misses = set()
        self.hit = []

    def add_ship(self, ship):
        """
        Add a Ship to the grid at the end of the ships list if it does not
        collide with other ships already there
        """
        justify_number = 0
        for position1 in ship.positions:
            for ship_1 in self.ships:
                if position1 in ship_1.positions:
                    justify_number = 1
        if justify_number == 1:
            pass
        if justify_number == 0:
            self.ships.append(ship)

    def shoot(self, position):
        """Shoot at the given position."""
        for ship in self.ships: # This structrue is the hit from TA and which leads to class BlindGrid that I use for sentense for the self.sunken_ship
            ship_result = ship.take_shot(position)
            if ship_result == 'HIT':
                self.hit.append(position)
                return ('HIT', None)
            elif ship_result == 'DESTROYED':
                self.hit.append(position)
                return ('DESTROYED', ship)
        self.misses.add(position)
        return ('MISS', None)

    def random_ship(self):
        ship_direction = random.randint(
            0, 1)  # We call 0 is on the y direction, 1 is on the x direction
        ship_type = random.randint(0, 4)
        ship_name = ship_types[ship_type][0]
        ship_leng = ship_types[ship_type][1]
        ship_posi = set()

        if ship_direction == 1:  # Ship lie on  y direction
            res_length = self.y_size - ship_leng
            start_posi = random.randint(0, res_length)
            for i in range(ship_leng):
                ship_posi.add((start_posi, i))
        elif ship_direction == 0:  # Ship lie on  x direction
            res_length = self.x_size - ship_leng
            start_posi = random.randint(0, res_length)
            for i in range(ship_leng):
                ship_posi.add((i, start_posi))

        return Ship(ship_name, ship_posi)

    def create_random(self, n):
        """I tried to used for i in range(n) but it didn't works since has problems with the index i and the output is less than the input
    , So junyuan told me use while sentence is a more conveninet way to solve this problem"""
        len1 = 0
        while True:
            b = self.random_ship()
            self.add_ship(b)
            len1 = len(self.ships)
            if len1 == n:
                break

class BlindGrid:
    """Encodes the opponent's view of the grid."""
    def __init__(self, grid):
        self.x_size = grid.x_size
        self.y_size = grid.y_size
        self.misses = grid.misses
        self.hits = set(grid.hit)
        self.sunken_ships = []
        for ship in grid.ships:
            if not ship.is_afloat():
                self.sunken_ships.append(ship)



def create_ship_from_line(line):
    parts = line.split()
    ship_name = parts[0]
    ship_positions = set()
    for el in parts[1:]:
        ship_x = int(el.split(':')[0])
        ship_y = int(el.split(':')[1])
        ship_positions.add((ship_x, ship_y))
    return Ship(ship_name, ship_positions)


def load_grid_from_file(filename):
    with open(filename, 'r') as file:
        coords = file.readline().strip()
        grid_x = int(coords.split(':')[0])
        grid_y = int(coords.split(':')[1])
        grid1 = Grid(grid_x, grid_y)
        for line in file:
            grid1.ships.append(create_ship_from_line(line))

    return grid1