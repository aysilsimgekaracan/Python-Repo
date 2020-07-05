# 6 kyu
# Playing with digits
# https://www.codewars.com/kata/5552101f47fc5178b1000050/solutions/python

def dig_pow(n, p):
    str_num = str(n)
    sum = 0

    for i in range(len(str_num)):
        sum += int(str_num[i]) ** p
        p += 1

    if sum % n == 0:
        k = sum / n
        return k
    else:
        return -1

