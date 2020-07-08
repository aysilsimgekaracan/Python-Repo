# 7 kyu
# Two to One
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

letters = ["abcdefghijklmnopqrstuvwxyz"]
def longest(s1, s2):
    return ''.join(sorted(set(s1).union(set(s2))))