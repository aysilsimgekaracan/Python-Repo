# 7 kyu
# Find the next perfect square!
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math
def find_next_square(sq):
    if math.sqrt(sq) % 1 != 0:
        return -1
    
    return (math.sqrt(sq) + 1) ** 2