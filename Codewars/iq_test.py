# 6 kyu
# IQ Test
# https://www.codewars.com/kata/552c028c030765286c00007d/train/python

def iq_test(numbers):
    numbers_lst = numbers.split(' ')
    
    even_integers = [number for number in numbers_lst if int(number) % 2 == 0]
    odd_integers = [number for number in numbers_lst if int(number) % 2 != 0]

    return numbers_lst.index(even_integers[0]) + 1 if len(even_integers) == 1 else numbers_lst.index(odd_integers[0]) + 1
