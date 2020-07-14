# 7 kyu
# Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])