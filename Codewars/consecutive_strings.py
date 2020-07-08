# 6 kyu
# Consecutive strings
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python


def longest_consec(strarr, k):
    res = ""
    for i in range(len(strarr) - k + 1):
        max_str = ""
        max_str = strarr[i: k+i]

        if len(max_str) > len(res):
            res = max_str

    return res
