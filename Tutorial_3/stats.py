#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSE101 - Computer Programming 
Tutorial 3 - CSE101 Statistics
Created on Wed Sep 29 21:01:01 2021

@author: Yubo Cai
"""


# Exercise 1 - Computing Averages
def average(numlist):
    return round(sum(numlist) / len(numlist), 2)


# Exercise 2 - Convert a string of floats to a list
def string_floats_to_list(string_floats):
    """Return a list from the string of floats string_floats."""
    lis = string_floats.split(' ')
    return lis


# Exercise 3 - Student Data
def student_data(data_string):
    """Compute (name, results) tuple from the string data_string."""
    name, num = data_string.split(' ')[0], data_string.split(' ')[1:]
    for i in range(len(num)):
        num[i] = float(num[i])

    return (name, num)


# Exercise 4 - Convert a tuple to a string
def tuple_to_string(name, results):
    """Return string from (name, results) tuple"""
    for i in range(len(results)):
        results[i] = str(results[i])

    return name + ' ' + ' '.join(results)


# Exercise 5 - Reading Student Data
def read_student_data(filename):
    """Return list of student data from file"""
    with open(filename, 'r') as f:
        return [student_data(line.strip()) for line in f]


# Exercise 6 - Extracting Averages
def extract_averages(filename):
    """Return list of name and average for each line in file"""
    data = read_student_data(filename)
    result = []

    for i in range(len(data)):
        ave = 0
        for j in range(len(data[i][1])):
            ave += float(data[i][1][j])
        ave = round(ave / len(data[i][1]), 2)
        result.append((data[i][0], ave))

    return result


# Exercise 7 - Filtering Lists of Scores
def discard_scores(numlist):
    """Filter numlist: construct a new list from numlist with
    the first two, and then the lowest two, scores discarded.
    """
    lis = numlist[2:]
    for _ in range(2):
        lis.remove(min(lis))

    return lis


# Exercise 8 - Summaries per Student
def summary_per_student(infilename, outfilename):
    """Create summaries per student from the input file 
    and write the summaries to the output file.
    """
    data = read_student_data(infilename)
    total_num = 0
    with open(outfilename, 'w') as f:
        for i in range(len(data)):
            sum_num = round(sum(discard_scores(data[i][1])), 2)
            total_num += sum_num
            lis = discard_scores(data[i][1])
            f.write(
                tuple_to_string(data[i][0], lis) + ' sum: ' + str(sum_num) +
                '\n')

        f.write('total average: ' + str(round(total_num / len(data), 2)))


# Exercise 9 - Summaries per Tutorial
def summary_per_tutorial(infilename, outfilename):
    """Create summaries per student from infile and write to outfile."""
    data = read_student_data(infilename)
    with open(outfilename, 'w') as f:
        for i in range(len(data[0][1])):
            lis = []
            for j in range(len(data)):
                lis.append(data[j][1][i])
            ave_num = average(numlist=lis)
            min_num = min(lis)
            max_num = max(lis)
            f.write(
                f'TD {i + 1}: average: {ave_num}, min: {min_num}, max: {max_num}\n'
            )


# Exercise 10 - Sending Results to Students
def generate_emails(filename):
    """Generate emails to students with their results"""
    data = read_student_data(filename)
    for i in range(len(data)):
        with open(data[i][0] + '.txt', 'w') as f:
            f.write(f'To: {data[i][0]}@polytechnique.edu\n\n')
            f.write(
                'This is to notify you of your final results for the CSE101 course, see\ntable below.  (Note that the two first and two lowest scores are\nexcluded from the result.)\n\n'
            )

            string = ''
            for j in range(len(data[i][1])):
                string += f'TD{j+1}  '
            string += 'Result\n'
            f.write(string)

            string2 = ''
            for j in range(len(data[i][1])):
                string2 += f'-----'
            string2 += '------\n'
            f.write(string2)

            string3 = ''
            for j in range(len(data[i][1])):
                string3 += f'{data[i][1][j]}  '
            string3 += str(round(sum(discard_scores(data[i][1])), 2))
            f.write(string3 + '\n\n')

            f.write('Best regards,\n')
            f.write('and please get back to me if you have any questions,\n')
            f.write('Your Teacher')