#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:08:27 2021

@author: Yubo Cai
"""

import random


# Exercise 1
def is_palindrome(word):
    """Check if input is a palindrome."""
    if word == '' or len(word) == 1:
        return True
    if word[0] == word[-1]:
        if len(word) <= 2:
            return True
        else:
            list_1 = word[1:-1]
            return is_palindrome(list_1)
    else:
        return False


# Exercise 2
def rec_pow(a, b):
    """Compute a**b recursively"""
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        base1 = pow(rec_pow(a, b / 2), 2)
        return int(base1)
    else:
        base2 = pow(rec_pow(a, (b - 1) / 2), 2) * a
        return int(base2)


def even(n):
    """Return True if and only if the given number is even."""
    if n == 0:
        return True
    if n == 1:
        return False
    return even(n - 2)


# Exercise 3
def binary_search(sorted_list, lower, upper, element):
    """Return the position of the element in the sublist of sorted_list
    starting at position lower up to (but excluding) position upper 
    if it appears there. Otherwise return -1.
    """

    if len(sorted_list[lower:upper]) == 0:
        return -1
    elif len(sorted_list[lower:upper]) == 1:
        if sorted_list[lower:upper][0] == element:
            return lower
        elif sorted_list[lower:upper][0] != element:
            return -1

    if (upper - lower) % 2 == 0:
        mid = int((upper + lower) / 2)
    else:
        mid = int((upper + lower + 1) / 2)

    if sorted_list[mid] == element:
        return mid

    elif sorted_list[mid] > element:
        return binary_search(sorted_list, lower, mid, element)

    else:
        return binary_search(sorted_list, mid + 1, upper, element)
    """ Hint from https://www.geeksforgeeks.org/python-program-for-binary-search/ and Junyuan Wang, actually this question spend me tons of time even with those
    hints since we don't know when the mid is odd number whether we should round up or round down so I spend tons of time on adjusting the index"""


def random_increasing_integer_sequence(length):
    """Return an increasing list of integers of the given length."""
    current = 0
    res = []
    for i in range(length):
        current += random.randint(1, 10)
        res.append(current)
    return res


def pp_words():
    with open('sortedpp.txt') as file:
        return [w.strip() for w in file]


def read_positive_integer(text, position):
    """Read a number starting from the given position, return it and the first
    position after it in a tuple. If there is no number at the given position
    then return None.
    """
    if text[position].isdigit() is False:
        return None
    """ https://www.w3schools.com/python/ref_string_isdigit.asp with the method of how to judge whether is digital"""

    index = position
    string1 = ''
    for i in range(len(text) - position):
        if text[index].isdigit() is True:

            string1 += text[index]
            index += 1

    return (int(string1), index)


def evaluate(expression, position):
    """Evaluate the expression starting from the given position.
    Return the value and the first position after the read
    sub-expression. If the string starting at the given expression
    is not an arithmetic expression, return None.
    """
    dig_all = [
        '+', '-', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '0'
    ]
    op = ['+', '-', '*']

    if expression[position] not in dig_all:
        return None
    # Testify whether the element on the position is in dig_all or not

    expression = expression[position:]
    # delete the useless parts

    a = []
    for i in range(len(expression)):
        if expression[i] in dig_all:
            a.append(expression[i])

    if expression[0] == '(' and expression[-1] == ')':
        expression = expression[1:-1]
    # get rid of the useless bracket

    pure_number = 0
    for el in expression:
        if el.isdigit() is False:
            pure_number = 1

    if pure_number == 0:
        return read_positive_integer(expression, 0)
    # We try to find the pure number

    is_inbracket = 0
    num_bracket = 0
    index2 = 0
    while index2 < len(expression):
        h = expression[index2]
        if is_inbracket == 0 and h in op:
            break
        if h == '(':
            num_bracket += 1
        if h == ')':
            num_bracket -= 1
        if num_bracket == 0:
            is_inbracket = 0
        elif num_bracket != 0:
            is_inbracket = 1

        index2 += 1

    part1 = expression[0:index2]
    part2 = expression[index2 + 1:]
    if expression[index2] == op[0]:
        return (evaluate(part1, 0)[0] + evaluate(part2, 0)[0],
                len(a) + position)
    elif expression[index2] == op[1]:
        return ((evaluate(part1, 0)[0]) - (evaluate(part2, 0)[0]),
                len(a) + position)
    elif expression[index2] == op[2]:
        return (evaluate(part1, 0)[0] * evaluate(part2, 0)[0],
                len(a) + position)

"""This question is way more difficult for me and the solution logic of this question to find the special operation like + - * is told by 
Junyuan Wang but the operation of finding the special operation is differenet but still this question is too difficult for me """
