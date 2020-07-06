# 7 kyu
# Isograms
# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    string = string.lower()
    for c in string:
        if string.count(c) == 1:
            pass
        else:
            return False
        
    return True