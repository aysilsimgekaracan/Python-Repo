# 7 kyu
# Growth of a Population
# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

def nb_year(p0, percent, aug, p):
    year = 0
    percent = percent / 100
    while p0 < p:
        p0 = p0 + p0 * percent + aug
        year += 1
    return year