# 6 kyu
# Are they the "same"?
# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    array1 = [number**2 for number in array1]
    return True if sorted(array1) == sorted(array2) else False