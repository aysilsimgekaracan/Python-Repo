# 6 kyu
# Find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836


def find_it(seq):
    used = []
    count = 0
    for digit in seq:
        if not digit in used:
            for dgt in seq:
                if digit == dgt:
                    count += 1
            if count % 2 != 0:
                return digit