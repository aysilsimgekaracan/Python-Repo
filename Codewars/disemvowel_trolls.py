# 7 kyu
# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string):
    wowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([c for c in string if c.lower() not in wowels])