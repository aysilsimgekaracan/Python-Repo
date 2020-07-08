# 7 kyu
# List Filtering
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    return [i for i in l if type(i) != str]