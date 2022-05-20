#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 23:54:19 2021

@author: apple
"""

from numpy import *

# Exercise 1
def average(numlist):
    """Return average of list of numbers"""
    ave = mean(numlist)
    return round(ave,2)

# Exercise 2
def string_floats_to_list(string_floats):
    """Return a list from the string of floats string_floats."""
    sep = string_floats.split()
    a_float = []
    for num in sep:
        a_float.append(float(num))
    return a_float

# Exercise 3
def student_data(data_string):
    """Compute (name, results) tuple from the string data_string."""
    data = data_string.split()
    login_name = data[0]
    result = []
    for i in range(1,len(data)):
        result.append(float(data[i]))
    return (login_name, result)

# Exercise 4
def tuple_to_string(name, results):
    """Return string from (name, results) tuple"""
    name_input = name
    sep_result = ' '.join([str(x) for x in results])
    return (name_input + ' ' + sep_result)

# Exercise 5
def read_student_data(filename):
    """Return list of student data from file"""
    list_1 = []
    with open(filename,'r') as file:
        for line in file:
            list_1.append(student_data(line))
    return list_1

# Exercise 6
def extract_averages(filename):
    """Return list of name and average for each line in file"""
    a = read_student_data(filename)
    s = []
    for t in a:
        s.append((t[0],average(t[1])))
    return s

# Exercise 7
def discard_scores(numlist):
    """Filter numlist: construct a new list from numlist with
    the first two, and then the lowest two, scores discarded.
    """
    numl = [num for num in numlist]
    for i in range(2):
        numl.remove(numl[0])

    for i in range(2):
        mini = numl[0]
        for i in range(len(numl)):
            if mini > numl[i]:
                mini = numl[i]
                i = i + 1
        numl.remove(mini)
        
    return numl

def summary_per_student(infilename, outfilename):
    """Create summaries per student from the input file 
    and write the summaries to the output file.
    """
    # I receive the hint from Junyuan Wang
    
    list_out = []
    whole_sum_student = 0
    data = read_student_data(infilename)
    for student in data:
        name_part = tuple_to_string(student[0], discard_scores(student[1]))
        sum_student = 0
        for num in discard_scores(student[1]):
            sum_student += num
        whole_sum_student += sum_student
        number_part = 'sum: ' + str(round(sum_student,2))
        data_person = name_part + ' ' + number_part
        list_out.append(data_person)
        
    total_ave = round(whole_sum_student/len(list_out),2)
    str_total = 'total average: ' + str(total_ave)
    list_out.append(str_total)
    
    with open(outfilename, 'w') as sample:
        for line in list_out:
            sample.write(line + '\n')
            
def summary_per_tutorial(infilename, outfilename):
    """Create summaries per student from infile and write to outfile."""
    
    data = read_student_data(infilename)
    l = []
    for i in range(len(data[0][1])):
        column = []
        
        for j in range(len(data)):
            td_score = data[j][1][i]
            column.append(td_score)
            
        ave_td = average(column)
        max_td = max(column)
        min_td = min(column)
       
        l.append('TD' + str(i+1) +': average: ' + str(ave_td) + ' min: ' + str(min_td) + ' max: ' + str(max_td))
    
    with open(outfilename, 'w') as sample_2:
        for line in l:
            sample_2.write(line + '\n')
        
