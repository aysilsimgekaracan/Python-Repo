# 6 kyu
# Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    count = 0
    check_list = []
    temp = []
    text = text.lower()
    for i in range(len(text) - 1):
        if not text[i] in check_list:
            check_list.append(text[i])
            temp = text[i+1::]
            if text[i] in temp:
                count += 1
        else:
            pass

    return count