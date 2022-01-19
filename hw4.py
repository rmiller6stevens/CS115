from random import randrange
from functools import reduce
def change(amount,coins):
#Intake is a value that must be reached  using the values in the list "coins"
    if amount == 0:
        return 0
    elif len(coins) == 0:
        return float("inf")
    elif amount < 0:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        no = change(amount,coins[1:])
        yes = change(amount - coins[0],coins) + 1
        return min(no,yes)

#==================
def check(lst):
    if len(lst) == 1:
        return True
    t = lst[0]
    checks = reduce(lambda x,y: True if y != t else False,lst)
    if checks == True:
        lst = lst[1:]
        return check(lst)
    else:
        return False
def currency(length):
#intake is an integer of length, then it will return a list with random non-equal inegers
    if length <= 0:
        return []
    lst = list(range(length))
    final =list(map(lambda x: x + randrange(10),lst))
    if len(final) > 1:
        if check(final) == True:
            return final
        else:
            return currency(length)
    else:
        return final
