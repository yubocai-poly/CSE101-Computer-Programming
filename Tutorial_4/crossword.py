#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:59:16 2021

@author: Yubo Cai
"""
# Exercise 1
def split_type(line):
    """Splits off the first word in the line and returns both parts in a tuple.
    Also eliminates all leading and trailing spaces.
    Example:
        split_type('ROW ##.##') returns ('ROW', '##.##')
        split_type('CLUE (0,1) down: Of or pertaining to the voice (5)') returns
            ('CLUE', '(0,1) down: Of or pertaining to the voice (5)')
        split_type('  ROW    ##.##   ') returns ('ROW', '##.##') """
        
    line= line.strip()
    cut_position = line.index(' ')
    return(line[:cut_position].strip(), line[cut_position:].strip())

# Exercise 2
def read_row(row):
    """Reads a row of a crossword puzzle and decomposes it into a list. Every
    '#' is blocking the current box. Letters 'A', ..., 'Z' and 'a', ..., 'z'
    are values that are already filled into the box. These letters are capitalized
    and then put into the list. All other characters stand
    for empty boxes which are represented by a space ' ' in the list.
    Examples:
        read_row('#.#') gives ['#', ' ', '#']
        read_row('C.T') gives ['C', ' ', 'T']
        read_row('cat') gives ['C', 'A', 'T']
    """
    row_read = []
    for characters in row:
        if characters == '#':
            row_read.append(characters)
        elif characters.isalpha():
            row_read.append(characters.upper())
        else:
            row_read.append(' ')
    return row_read

# Exercise 3
def coord_to_int(coordstring):
    """Reads a coordinate into a couple in the following way: The input is of the form
        '(x,y)' where x, y are integers. The output should then be
        (x, y), where (x, y) is a tuple of values of type int.
    None of these values are strings.
    Example:
        coord_to_int('(0,1)') returns
        (0, 1) 
    """
    
    left_coor = coordstring.strip('(')
    end_coor = left_coor.strip(')')
    m = end_coor.index(',')
    x_position = int(end_coor[:m])
    y_position = int(end_coor[(m+1):])
    return(x_position , y_position)

# Exercise 4    
def read_clue(cluestring):
    """Reads a clue into a tuple in the following way: The input is of the form
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
    
    sep_1 = cluestring.split(':')
    coordinate = coord_to_int((sep_1[0].split(' '))[0])
    direction = sep_1[0][(sep_1[0].index(')'))+1:].strip()
    sep_part2 = sep_1[1].strip()
    description = sep_part2[:sep_part2.index('(')].strip()
    len_word = int(sep_part2[(sep_part2.index('(')+1):sep_part2.index(')')])
    return (coordinate, direction, len_word, description)

# Exercise 5
def read_file(filename):
    """Opens the file with the given filename and creates the puzzle in it.
    Returns a pair consisting of the puzzle grid and the list of clues. Assumes
    that the first line gives the size. Afterwards, the rows and clues are given.
    The description of the rows and clues may interleave arbitrarily.
    """
    
    grid = []
    clues = []
    with open(filename) as input_file:
        for line in input_file:
            type_grid, info = split_type(line)
            if type_grid == 'SIZE':
                pass
            elif type_grid == 'ROW':
                grid.append(read_row(info))
            elif type_grid == 'CLUE':
                clues.append(read_clue(info))
    return(grid,clues)
    
# Exercise 6
def create_clue_string(clue):
    """ Given a clue, which is a tuple
    (position, direction, length, question),
    create a string in the form 'position direction: question (length)'.
    For example, given the clue
        ((2, 3), 'across', 4, 'Black bird'),
    this function will return
        '(2,3) across: Black bird (4)'
    """
    return f'({str(clue[0][0])},{str(clue[0][1])}) {clue[1]}: {clue[3]} ({clue[2]})'

# Exercise 7
def create_grid_string(grid):
    """Return a crossword grid as a string."""
    size = len(grid)
    separator = '  +' + ('-----+')*size
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
    cl = create_grid_string(grid)
    
    cl += '\n'
    for clue in clues:
        cl += create_clue_string(clue) +'\n'
        
    return cl[:-1]

# Exercise 8
def fill_in_word(grid, word, position, direction):
    """Create and return a new grid (a list of lists) based on the grid
    given in the arguments, but with the given word inserted according
    to position and direction.
        - direction: is either 'down' or 'across'.
        - position: the coordinates of the first letter of the word in the grid.
    *This function may modify its grid argument!*
    """
    x_posi = position[0]
    y_posi = position[1]
    for i in range(len(word)):
        if direction == 'across':
            grid[x_posi][y_posi + i] = word[i]
        if direction == 'down':
            grid[x_posi + i][y_posi] = word[i]
    return grid

# Exercise 9
def create_row_string(row):
    """Returns a row representation of a string.
    Example:
        create_row_string(['#', 'A', ' ']) returns '#A.'
    """
    sily_B = ''
    for el in row:
        if el == '#':
            sily_B += el
        if el.isalpha():
            sily_B += el.upper()
        if el == ' ':
            sily_B += '.'
    return sily_B

# Exercise 10
def write_puzzle(filename, grid, clues):
    """Writes the puzzle given by the grid and by the clues to the specified
    file.
    """
    
    with open(filename, 'w') as output_file:
        output_file.write('SIZE '+ str(len(grid)) + '\n')
                          
        for row in grid:
            output_file.write(f'ROW {create_row_string(row)}' + '\n')
            
        for clue in clues:
            output_file.write(f'CLUE {create_clue_string(clue)}' + '\n')
    

        
    
    
    