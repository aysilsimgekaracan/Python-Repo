# 7 kyu
# Complementary DNA
# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    DNA = {'A': 'T',
           'T': 'A',
           'G': 'C',
           'C': 'G'}

    return ''.join([DNA.get(i) for i in dna])
