# 7 kyu
# Sum of odd numbers
# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

def row_sum_odd_numbers(n):
    lst = []
    x = 1
    for i in range(0, n*(n+1)//2):
        lst.append(x)
        x += 2
    return sum(lst[len(lst)-n:])