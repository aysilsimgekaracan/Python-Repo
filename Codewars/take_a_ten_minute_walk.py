# 6 kyu
# Take a Ten Minute Walk
# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    return False if len(walk) != 10 or walk.count('n') != walk.count('s') or walk.count('w') != walk.count('e') else True