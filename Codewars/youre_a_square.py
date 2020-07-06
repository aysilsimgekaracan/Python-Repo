# 7 kyu
# You're a square!
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

import math
def is_square(n):
    if n < 0:
        return False  
    return math.sqrt(n).is_integer()