# 6 kyu
# Multiples of 3 or 5
# https://www.codewars.com/kata/514b92a657cdc65150000006


def solution(number):
    sm = 0
    for i in range(number):
        if i % 3 == i % 5 == 0:
            sm += i
        elif i % 3 == 0 or i % 5 == 0:
            sm += i
    return sm