# 6 kyu
# Bit Counting
# https://www.codewars.com/kata/526571aae218b8ee490006f4

def countBits(n):
    return int(str(bin(n)).count('1'))