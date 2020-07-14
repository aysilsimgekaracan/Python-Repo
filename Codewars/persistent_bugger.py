# 6 kyu
# Persistent Bugger.
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    count = 0
    while n > 9:
        n_lst = [int(number) for number in str(n)]
        n = 1
        for num in n_lst:
            n *= num
        count += 1

    return count