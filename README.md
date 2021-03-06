# CSE-101 Computer Programming

## 📚 Professors
- [Ben smith](https://www.lix.polytechnique.fr/~smith/)

## 📚 Course Organization
- 14 lectures (1.5h) and 14 Tutorials (2h) 49 hours in total with 5 ECTS

## 📚 Course Arrangement
- LEC 0: Transition tutorial
- LEC 1: Functions and conditions
- LEC 2: Tuples, lists, and iteration
- LEC 3: String manipulation and file I/O
- LEC 4: Strings and f-strings
- LEC 5: Dictionaries
- LEC 6: Objects and Classes
- LEC 7: Modules
- LEC 8: Collections of objects
- LEC 9: Thinking about objects
- LEC 10: Abstraction, encapsulation... and execution
- LEC 11: Functions as objects
- LEC 12: Recursion
- LEC 13: Recursive Data Structures
- LEC 14: Callbacks

## ✏️ Project Sample - Sudoku
- This is the program you trying to use python and Tkinker to create the Sudoku game.
<img src="img/cse101.png" width = "600px" />

Code sample:
```python
# -*- coding: utf-8 -*-

class Sudoku:
    def __init__(self, filename):
        """Initilize rows, columns and squares as empty."""
        self.board = [([0]*9).copy() for _ in range(9)]
        self.read_board(filename)
        
    def read_board(self, filename):
        """Read a board from the given file."""
        with open(filename) as file:
            for (x, line) in enumerate(file):
                for (y, element) in enumerate(line):
                    if element in '123456789':
                        self.put(x, y, int(element))
                        
    def __str__(self):
        """Give a string representation of the board."""
        res = ''
        for x in range(9):
            if x == 0:
                res += '┌───┬───┬───┐\n'
            if x == 3 or x == 6:
                res += '├───┼───┼───┤\n'
            for y in range(9):
                if y % 3 == 0:
                    res += '│'
                if self.board[x][y] != 0:
                    res+=str(self.board[x][y])
                else:
                    res+='.'
            res+='│\n'
        res += '└───┴───┴───┘\n'
        return res

    def put(self, row, column, value):
        """Set value in cell (x,y)."""
        self.board[row][column] = value
        
    def delete(self, row, column):
        """Delete content of cell (x,y)."""
        self.board[row][column] = 0

    def check_row(self, row, value):
        """Return True if the value is already contained in the row."""
        return value in self.board[row]
    
    def check_column(self, column, value):
        """Return True if the value is already contained in the column."""
        for row in self.board:
            if value == row[column]:
                return True
        return False
    
    def check_box(self, row, column, value):
        """Return True if the 3x3 box that contains the cell with the given
        row and column contains already value.
        """
        for x in range(row//3*3, row//3*3 + 3): 
            for y in range(column//3*3, column//3*3 + 3):
                if value == self.board[x][y]:
                    return True
        return False
    
    def check(self, row, column, value):
        """Return True if the value is already in the row, column or box of
        the given cell."""
        return self.check_row(row, value) or \
            self.check_column(column, value) or \
            self.check_box(row, column, value)
        
    def find_first_empty(self):
        """Return the first empty cell if there is one, otherwise None."""
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    return (x,y)
        return None
    
    def solve(self):
        """Solve the given Sudoku. When a solution is found, print 'Found solution!'
        followed by the solution in the next line.
        """

        if self.find_first_empty() is None:
            print('Found solution!')
            print(self)
            return None
        
     
        row = self.find_first_empty()[0]
        col = self.find_first_empty()[1]
        for i in range(1, 10):
            if self.check(row, col , i) is False:
                self.put(row, col, i)
                self.solve()
                self.delete(row, col)
                
        # Like the hits in the exercise i use for sentense to solve this questtion
```

## 📚 Tools of this course
JupyterLab, Python, TKinker, Spyder

## 📚 Copyright
Copyright by Ben Smith, Yubo Cai, Ecole Polytechnique