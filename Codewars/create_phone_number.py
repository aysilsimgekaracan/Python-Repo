# 6 kyu
# Create Phone Number
# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python


def create_phone_number(n):
    return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(*n)