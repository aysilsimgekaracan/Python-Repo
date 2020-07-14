# 6 kyu
# Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    even_integers = []
    odd_integers = []
    for item in integers:
        if item % 2 == 0:
            even_integers.append(item)
        else:
            odd_integers.append(item)
    
    if len(even_integers) == 1:
        return int(even_integers[0])
    else:
        return int(odd_integers[0])