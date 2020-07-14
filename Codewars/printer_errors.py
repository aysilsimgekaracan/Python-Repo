# 7 kyu
# Printer Errors
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python


def printer_error(s):
    m_to_z = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    errors = [error for error in s if error in m_to_z]
    return "{}/{}".format(len(errors), len(s))