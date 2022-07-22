#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSE101 - Computer Programming 
Tutorial 4 - Crossword puzzles
Created on Wed Sep 29 21:01:01 2021

@author: Yubo Cai
"""


# Exercise 1 - Split off the type
def split_type(line):
    """
    Splits off the first word in the line and returns both parts in a tuple.
    Also eliminates all leading and trailing spaces.
    Example:
        split_type('ROW ##.##') returns ('ROW', '##.##')
        split_type('CLUE (0,1) down: Of or pertaining to the voice (5)') returns
            ('CLUE', '(0,1) down: Of or pertaining to the voice (5)')
        split_type('  ROW    ##.##   ') returns ('ROW', '##.##') 
    """
    string1 = line.strip().split(' ', 1)[0].strip()
    string2 = line.strip().split(' ', 1)[1].strip()
    return (string1, string2)


# Exercise 2 - Reading Rows
def read_row(row):
    """
    Reads a row of a crossword puzzle and decomposes it into a list. Every
    '#' is blocking the current box. Letters 'A', ..., 'Z' and 'a', ..., 'z'
    are values that are already filled into the box. These letters are capitalized
    and then put into the list. All other characters stand
    for empty boxes which are represented by a space ' ' in the list.
    Examples:
        read_row('#.#') gives ['#', ' ', '#']
        read_row('C.T') gives ['C', ' ', 'T']
        read_row('cat') gives ['C', 'A', 'T']
    """
    lis = []
    for el in row:
        if el.isalpha() or el == '#':
            lis.append(el.upper())
        else:
            lis.append(' ')

    return lis


# Exercise 3 - Reading coordinates
def coord_to_int(coordstring):
    """
    Reads a coordinate into a couple in the following way: The input is of the form
        '(x,y)' where x, y are integers. The output should then be
        (x, y), where (x, y) is a tuple of values of type int.
    None of these values are strings.
    Example:
        coord_to_int('(0,1)') returns
        (0, 1) 
    """
    num1 = coordstring.strip().split(',')[0].strip()
    num2 = coordstring.strip().split(',')[1].strip()
    return (int(num1[1:]), int(num2[:-1]))


# Exercise 4 - Reading clues
def read_clue(cluestring):
    """
    Reads a clue into a tuple in the following way: The input is of the form
        '(x,y) direction: question (length)'
    where x, y and length are integers, direction is 'across' or 'down'
    and question is the text of the clue. The output should then be
        ((x, y), direction, length, question)
    where (x, y) is a tuple of values of type int and length is of type int.
    There may be arbitrarily many spaces between the different parts of the input.
    Example:
        read_clue('(0,1) down: Of or pertaining to the voice (5)') returns
        ((0, 1), 'down', 5, 'Of or pertaining to the voice')
    """
    # 我们首先找坐标
    sep1 = cluestring.strip().split(' ', 1)
    coordinate = coord_to_int(sep1[0].strip())

    # 接下来找方向
    sep2 = sep1[1].strip().split(':')
    direction = sep2[0].strip()

    # 接下来找具体描述
    sep3 = sep2[1].strip().split('(', 1)
    information = sep3[0].strip()

    # 接下来找长度
    length = int(sep3[1].strip()[:-1])

    return (coordinate, direction, length, information)


# Exercise 5 - Reading input files
def read_file(filename):
    """
    Opens the file with the given filename and creates the puzzle in it.
    Returns a pair consisting of the puzzle grid and the list of clues. Assumes
    that the first line gives the size. Afterwards, the rows and clues are given.
    The description of the rows and clues may interleave arbitrarily.
    """
    with open(filename, 'r') as infile:
        grid = []
        clues = []
        for line in infile:
            line1 = line.strip().split(' ', 1)
            if line1[0] == 'SIZE':
                continue
            elif line1[0] == 'ROW':
                grid.append(read_row(line1[1].strip()))
            elif line1[0] == 'CLUE':
                clues.append(read_clue(line1[1].strip()))

        return (grid, clues)


# Exercise 6 - Creating clue strings
def create_clue_string(clue):
    """ 
    Given a clue, which is a tuple
    (position, direction, length, question),
    create a string in the form 'position direction: question (length)'.
    For example, given the clue
        ((2, 3), 'across', 4, 'Black bird'),
    this function will return
        '(2,3) across: Black bird (4)'
    """
    return f'{clue[0]} {clue[1]}: {clue[3]} ({clue[2]})'


# Exercise 7 -  Creating puzzle strings
def create_grid_string(grid):
    """Return a crossword grid as a string."""
    size = len(grid)
    separator = '  +' + ('-----+') * size
    column_number_line = '   '
    column_number_line += ''.join(f' {j:2}   ' for j in range(size))
    result = f'{column_number_line}\n{separator}\n'
    for (i, row) in enumerate(grid):
        fill = '  |'
        centre_line = f'{i:2}|'
        for entry in row:
            if entry == '#':
                fill += '#####|'
                centre_line += '#####|'
            else:
                fill += '     |'
                centre_line += f'  {entry}  |'
        result += f'{fill}\n{centre_line}\n{fill}\n{separator}\n'
    return result


def create_puzzle_string(grid, clues):
    """Return a human readable string representation of the puzzle."""
    return create_grid_string(grid) + '\n' + '\n' + ' '.join(
        create_clue_string(clue) for clue in clues)


# Exercise 8 - Filling in words
def fill_in_word(grid, word, position, direction):
    """
    Create and return a new grid (a list of lists) based on the grid
    given in the arguments, but with the given word inserted according
    to position and direction.
        - direction: is either 'down' or 'across'.
        - position: the coordinates of the first letter of the word in the grid.
    *This function may modify its grid argument!*
    """
    # 先把word放到grid里面
    if direction == 'down':
        for i in range(len(word)):
            grid[position[0]][position[1]] = word[i]
            position = (position[0] + 1, position[1])
    elif direction == 'across':
        for i in range(len(word)):
            grid[position[0]][position[1]] = word[i]
            position = (position[0], position[1] + 1)
    return grid


# Exercise 9 - Creating row strings
def create_row_string(row):
    """
    Returns a row representation of a string.
    Example:
        create_row_string(['#', 'A', ' ']) returns '#A.'
    """
    result = ''
    for el in row:
        if el == '#':
            result += '#'
        elif el.isalpha():
            result += el.upper()
        elif el == ' ':
            result += '.'
    return result


# Exercise 10 - Writing the file
def write_puzzle(filename, grid, clues):
    """
    Writes the puzzle given by the grid and by the clues to the specified file.
    """
    with open(filename, 'w') as outfile:
        outfile.write(create_puzzle_string(grid, clues))

        for row in grid:
            outfile.write(f'ROW {create_row_string(row)}\n')

        for clue in clues:
            outfile.write(f'CLUE {create_clue_string(clue)}\n')
