# 6 kyu
# Tribonacci Sequence
# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    if n == 0:
        lst = []
    elif n <= 3:
        lst = [signature[i] for i in range(n)]
    else:
        lst = signature
        for i in range(3, n):
            lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3])
    
    return lst
