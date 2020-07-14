# 6 kyu
# Build a pile of Cubes
# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

def find_nb(m):
    sum = 0
    n = 0
    while sum < m:
        n += 1
        sum += n ** 3
    return n if sum == m else -1