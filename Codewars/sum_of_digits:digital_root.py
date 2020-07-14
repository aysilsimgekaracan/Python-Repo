# 6 kyu
# Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_total(n):
    sum = 0
    seen = set
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

def digital_root(x: int):
    seen = set()
    while x not in seen:
        seen.add(x)
        x = digital_total(x)
    return x