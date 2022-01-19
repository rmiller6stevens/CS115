# Created by Prof. Nicolosi & Dominick DiMaggio for CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Robert Miller
# Pledge: "I pledge on my Honor to obey the Stevens Honor Code"
##########################################
from math import floor

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week
# Input: 8-digit decimal number in the format of YYYYMMDD
# Saturday: 0, Sunday: 1... Friday: 6  
# Hint: Look at Zeller's congruence.
#       The floor() function may be helpful. (Ex: floor(5.5) = 5)

def getWeekday(timestamp):
    year = timestamp // 10000
    month_day = timestamp % 10000
    month = month_day // 100
    day = month_day % 100
    yoc = year%100
    century = abs(year // 100)
    dow = (day + 13*(month+1)//5 + yoc + yoc//4 + century//4 - 2*century)%7
    if dow == 0:
        fdow = 'Saturday'
    elif dow == 1:
        fdow = 'Sunday'
    elif dow == 2:
        fdow = 'Monday'
    elif dow == 3:
        fdow = 'Tuesday'
    elif dow == 4:
        fdow = 'Wednesday'
    elif dow == 5:
        fdow = 'Thursday'
    elif dow == 6:
        fdow = 'Friday'
    print(fdow +': ' + str(dow))

######################################################################
# Task 2: For this task, you will create an encoder and decoder
#         for a Caesar cipher using the map function.
# You may find this website helpful:
# https://cryptii.com/pipes/caesar-cipher

######################################################################
# This provided helper function may be useful
# Input: List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')     ('H   E   L   L   O')
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

######################################################################
# Encoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. HELLO WORLD, 3)
# Output: An encoded string            (Ex. KHOOR ZRUOG)
# Hint: The ord() function converts single-character strings to ASCII
def addition(n):
    def add(shift):
        return n + shift
    return add
def caesarEncoder(str, shift):
    test = list(str)
    test = list(map(ord, test))
    test = list(map(addition(shift), test))
    test = asciiToString(test)
    print(test)

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
def subtraction(n):
    def sub(shift):
        return shift-n
    return sub
def caesarDecoder(str, shift):
    test1 = list(str)
    test1 = list(map(ord, test1))
    test1 = list(map(subtraction(shift), test1))
    test1 = asciiToString(test1)
    print(test1)
