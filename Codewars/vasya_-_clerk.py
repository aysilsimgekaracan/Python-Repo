# 6 kyu
# Vasya - Clerk
# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python


def tickets(people):
    bill_25 = 0
    bill_50 = 0
    for dollar in people:
        if dollar == 25:
            bill_25 += 1
        elif dollar == 50:
            if bill_25 > 0:
                bill_25 -= 1
                bill_50 += 1
            else:
                return "NO"
        elif dollar == 100:
            if bill_50 > 0 and bill_25 > 0:
                bill_50 -= 1
                bill_25 -= 1
            elif bill_25 > 2:
                bill_25 -= 3
            else:
                return "NO"
    return "YES"