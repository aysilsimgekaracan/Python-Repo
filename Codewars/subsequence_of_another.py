# Beta - Average Assessed Rank: 6 kyu
# Subsequence of Another
# https://www.codewars.com/kata/5ab2b6abe78eee7de600361e/train/python

def subseq(needle, hay):
    needle_len = len(needle)
    hay_len = len(hay)
    
    while hay_len >= 0:

        if needle_len == 0:
            return True
        if hay_len == 0:
            return False

        if needle[needle_len - 1] == hay[hay_len - 1]:
            needle_len -= 1
            hay_len -= 1
        else:
            hay_len -= 1