#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:38:07 2021

@author: Yubo Cai
"""

# Exercise 1
def hello_world():
    return 'Hello world!' # use return instead of print according to the requirement

# Exercise 2
def check_day(n):
    """
    Given an integer between 1 and 7 inclusive,
    return either string 'work!' or string 'rest!'
    depending on whether the day is a workday or not
    """
    if n < 1 or n > 7:
        return None # invalid m
    elif n >= 1 and n < 6:
        return 'work!'
    else:
        return 'rest!'
    
# Exercise 3
def name_of_month(m):
    """Given an integer m between 1 and 12 inclusive,
    indicating a month of the year, returns the name of that month.
    For example: name_of_month(1) == 'January' and name_of_month(12) == 'December'.
    If the month does not exist (that is, if m is outside the legal range),
    then this function returns None.
    """
    if m < 1 or m > 12:  # Non-existent month
        return None
    elif m == 1:  
        return 'January'
    elif m == 2:  
        return 'February'
    elif m == 3:  
        return 'March'
    elif m == 4:  
        return 'April'
    elif m == 5:  
        return 'May'
    elif m == 6:  
        return 'June'
    elif m == 7:  
        return 'July'
    elif m == 8:  
        return 'August'
    elif m == 9:  
        return 'September'
    elif m == 10:  
        return 'October'
    elif m == 11:
        return 'November'
    elif m == 12:  
        return 'December'
    
# Exercise 4
def str_with_suffix(n):
    """Convert the integer n to a string expressing the corresponding 
    position in an ordered sequence.
    Eg. 1 becomes '1st', 2 becomes '2nd', etc.
    """
    
    if n % 10 == 1 and n % 100 != 11:
        suffix = 'st'
    elif n % 10 == 2 and n % 100 != 12:
        suffix = 'nd'
    elif n % 10 == 3 and n % 100 != 13:
        suffix = 'rd'
    else:
        suffix = 'th'
    return str(n) + suffix
    
# Exercise 5
def is_leap_year(y):
    """ Return True if y is a leap year, False otherwise. """

    if y % 100 == 0:
        if y % 400 == 0:
            return True
        return False
    if y % 4 == 0:
        return True
    else:
        return False

# Exercise 6
def number_of_days(m, y):
    """Returns the number of days in month m of year y."""
    con = is_leap_year(y)
    
    if m < 1 and m > 12:
        return None
    if m == 2:
        if con is True:
            return 29
        return 28
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        return 30

# Exercise 7
def date_string(n, m, y):
    """Returns the full sentense of month"""
    
    if n < 1 or m < 1 or m > 12:
        return 'Nonexistent date'
    if n > number_of_days(m, y): #If the month is more than the dates of the month supposed to be, it turns nonexistence
        return 'Nonexistent date'
    else:
        return 'The ' + str_with_suffix(n) + ' of ' +  name_of_month(m) + ', ' + str(y)  
   
# Exercise 8
def time_string(b):
    """ Convert the number of seconds to mins hours and dates"""
    
    """ Logic from my tutor, the days and hours, those four parts
    should operate independently or seperately. if it's zero then is empty"""
    
    sep = b # We use single equal to variable something, double equal dosen't change anything
    days = sep // 86400
    sep = sep % 86400
    hours = sep // 3600
    sep = sep % 3600
    minutes = sep // 60
    sep = sep % 60
    seconds = sep
    
    # Days 
    if days == 0:
        d_str = ''
    elif days == 1:
        d_str = str(days) + ' day, '
    else:
        d_str = str(days) + ' days, '
   
    # Hours
    if hours == 0:
        h_str = ''
    elif hours == 1:
        h_str = str(hours) + ' hour, '
    else:
        h_str = str(hours) + ' hours, '
        
    # Minutes
    if minutes == 0:
        m_str = ''
    elif minutes == 1:
        m_str = str(minutes) + ' minute, '
    else:
        m_str = str(minutes) + ' minutes, '
    
    # Seconds
    if seconds == 1:
        s_str = str(seconds) + ' second'
    else:
        s_str = str(seconds) + ' seconds'
  
    return d_str + h_str + m_str + s_str
   
        

    
    
    
        
    
    
    
        
    
   
    
   
    