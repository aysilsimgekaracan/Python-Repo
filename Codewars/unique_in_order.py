# 6 kyu
# Unique In Order
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    res = []
    previous = None
    for i in iterable:
        if i != previous:
            res.append(i)
        previous = i
    return res