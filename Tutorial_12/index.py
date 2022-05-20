#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 08:14:45 2022

@author: apple
"""


class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.key == other.key \
           and self.value == other.value \
           and self.left == other.left \
           and self.right == other.right

    def __repr__(self):
        return f'Node({repr(self.key)}, {repr(self.value)}, {repr(self.left)}, {repr(self.right)})'

    def __str__(self):
        lines, _ = self._str_aux()
        return '\n'.join(lines)

    # Exercise 2
    def search(self, key):
        if self.key == key:
            return self.value
        if self.key < key:  # means the value is bigger than the key so we search right
            if self.right is None:
                return None
            else:
                return self.right.search(key)
        if self.key > key:  # means the value is smaller than the key so we search left
            if self.left is None:
                return None
            else:
                return self.left.search(key)

    # Exercise 3
    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(f'{self.key}: {self.value}')
        if self.right is not None:
            self.right.print_in_order()

    """Hint from the tutorial: first, if node has a left child, recursively call print_in_order() on the left child;
    then, print the node’s key and value;
    finally, if node has a right child, recursively call print_in_order() on the right child."""

    # Exercise 4
    def add(self, key, value):
        if self.key == key:
            if value != self.value[-1]:
                self.value.append(value)
            else:
                return None

        if key < self.key:
            if self.left is None:
                list_1 = [value]
                new_node = Node(key, list_1, None, None)
                self.left = new_node
            else:
                self.left.add(key, value)

        if key > self.key:
            if self.right is None:
                list_2 = [value]
                new_node = Node(key, list_2, None, None)
                self.right = new_node
            else:
                self.right.add(key, value)

    # Exercise 6
    def write_in_order(self, filename):
        """Write all key: value pairs in the index tree
        to the named file, one entry per line.
        """
        with open(filename, 'w') as file:
            self.write_in_order_rec(file)

    def write_in_order_rec(self, file):
        """Recursive helper method for write_in_order."""
        """Hint from Junyuan Wang, he told me to consider this question from left and right sides and write the self into the file at first which has the
        same struction with the exercise 3"""

        if self.left is None:
            pass
        if self.left is not None:
            self.left.write_in_order_rec(file)

        file.write(f'{self.key}: {self.value}' + '\n')
        if self.right is None:
            pass
        if self.right is not None:
            self.right.write_in_order_rec(file)

    # Exercise 8
    def height(self):
        max_all = 0
        max_right = 0
        max_left = 0
        
        if self.left is None and self.right is None:
            return 0
        
        if self.left is None:
            max_right = 1 + self.right.height()
            return max_right
        
        if self.right is None:
            max_left = 1 + self.left.height()
            return max_left
        
        max_all = 1 + max(max_left, max_right)
        return max_all

    def _str_aux(self):
        # Recursive helper for __str__.
        # Returns lines (to be joined) and the horizontal position where
        # a branch from an eventual parent should be attached.
        label = f'{self.key}: {self.value}'

        # Leaf case
        if self.right is None and self.left is None:
            return [label], len(label) // 2

        if self.left is None:
            llines, lpos, lwidth, ltop0, ltop1, lfill = [], 0, 0, '', '', ''
        else:  # Recurse left
            llines, lpos = self.left._str_aux()
            lwidth = len(llines[0])
            ltop0 = lpos * ' ' + ' ' + (lwidth - lpos - 1) * '_'
            ltop1 = lpos * ' ' + '/' + (lwidth - lpos - 1) * ' '
            lfill = lwidth * ' '

        if self.right is None:
            rlines, rpos, rwidth, rtop0, rtop1, rfill = [], 0, 0, '', '', ''
        else:  # Recurse right
            rlines, rpos = self.right._str_aux()
            rwidth = len(rlines[0])
            rtop0 = rpos * '_' + ' ' + (rwidth - rpos - 1) * ' '
            rtop1 = rpos * ' ' + '\\' + (rwidth - rpos - 1) * ' '
            rfill = rwidth * ' '

        cfill = len(label) * ' '

        # Extend llines or rlines to same length, filling with spaces (or '')
        maxlen = max(len(llines), len(rlines))
        llines.extend(lfill for _ in range(maxlen - len(llines)))
        rlines.extend(rfill for _ in range(maxlen - len(rlines)))

        res = []
        res.append(ltop0 + label + rtop0)
        res.append(ltop1 + cfill + rtop1)
        res.extend(lline + cfill + rline
                   for (lline, rline) in zip(llines, rlines))

        return res, lwidth + len(label) // 2
    
    # Exercise 9 
    def list_in_order(self):
        lis = []
        self.write_in_order('list_in_order')
        with open('list_in_order', 'r') as infile:
            for line in infile:
                line_key = int(line.split(': ')[0])
                line_value = line.split(': ')[1][:-1]
                el = (line_key, line_value)
                lis.append(el)
        return lis
        """I tried to write the function in the following code but failed the test 2 and I couln't
        fix it however junyuan told i can use write_in_order to solve this question"""
                
        """if self.left is None and self.right is None:
            lis.append((self.key, self.value))
       
            
            
        if  self.left is not None:
            lis.append((self.key, self.value))
          
            self.left.list_in_order()
           
        if self.right is not None:
            lis.append((self.key, self.value))
          
            self.right.list_in_order()
        
        lis_helper = sorted(lis)
        for i in range(len(lis_helper)):
            if i == len(lis_helper) - 1:
                break
            if lis_helper[i] == lis_helper[i + 1]:
                lis_helper.pop(i)
        return sorted(lis_helper)"""
        # I tried to write it in this way but clearly it failed, so I find another methond with function write_in_order
            

            
def example_bst():
    n7 = Node(7, 'Seven', None, None)
    n13 = Node(13, 'Thirteen', None, None)
    n6 = Node(6, 'Six', None, n7)
    n3 = Node(3, 'Three', None, None)
    n14 = Node(14, 'Fourteen', n13, None)
    n4 = Node(4, 'Four', n3, n6)
    n10 = Node(10, 'Ten', None, n14)
    n8 = Node(8, 'Eight', n4, n10)
    root = n8
    return root
    # we start from the number 7 and give the links from 7


def split_in_words_and_lowercase(line):
    """Split a line of text into a list of lower-case words."""
    parts = line.strip('\n').replace('-',
                                     ' ').replace("'",
                                                  " ").replace('"',
                                                               ' ').split()
    parts = [p.strip('",._;?!:()[]').lower() for p in parts]
    return [p for p in parts if p != '']


# Exercise 5
def construct_bst_for_indexing(filename):
    nodes = []
    with open(filename, "r") as infile:
        for lines in infile.readlines():
            a = split_in_words_and_lowercase(lines)
            nodes.append(a)

    root = Node(nodes[0][0], [1], None, None)
    a = len(nodes)
    for i in range(a):
        for word in nodes[i]:
            root.add(word, i + 1)
    return root


# Exercise 7
def generate_index(textfile, indexfile):
    bts = construct_bst_for_indexing(textfile)
    bts.write_in_order(indexfile)


# Exercise 9
def balanced_bst(sorted_list):
    """Return balanced BST constructed from sorted list."""
    return balanced_bst_rec(sorted_list, 0, len(sorted_list))


def balanced_bst_rec(sorted_list, lower, upper):
    """Recursive helper function for balanced_bst."""
    index = int((lower + upper) / 2)
    if lower >= upper:  # since lower input shouldn't bigger than upper
        return None
    if lower + 1 == upper:
        return Node(sorted_list[lower][0], sorted_list[lower][1], None, None)
    left = balanced_bst_rec(sorted_list, lower, index)
    right = balanced_bst_rec(sorted_list, index + 1, upper)

    return Node(sorted_list[index][0], sorted_list[index][1], left, right)
