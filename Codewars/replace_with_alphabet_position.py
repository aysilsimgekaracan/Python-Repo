# 6 kyu
# Replace With Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da/solutions/python

import string

def alphabet_position(text):
    alphabet = dict(zip(string.ascii_lowercase, range(1,27)))
    text = text.lower()
    position_list = []
    for c in text:
        if c not in alphabet.keys():
            pass
        else:
            position_list.append(str(alphabet.get(c)))
    
    return ' '.join(position_list)
