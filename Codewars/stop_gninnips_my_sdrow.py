# 6 kyu
# Stop gninnipS My sdroW!
# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    lst = sentence.split(' ')
    for item in lst:
        if len(item) >= 5:
            index = lst.index(item)
            lst[index] = item[::-1]
    return ' '.join(lst)