# 6 kyu
# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c


def duplicate_encode(word):
    word = word.lower()
    str = ""
    for item in word:
        if word.count(item) > 1:
            str += ")"
        else:
            str += "("

    return str