# 6 kyu
# Equal Sides Of An Array
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    mult_r = 0
    mult_l = 0
    for i in range(len(arr)):
        temp_r = i + 1
        temp_l = i - 1
        while temp_r < len(arr):
            mult_r += arr[temp_r]
            temp_r += 1
        while  temp_l >= 0:
            mult_l += arr[temp_l]
            temp_l -= 1
            
        if mult_l == mult_r:
            return i
        else:
            mult_r = 0
            mult_l = 0  
            
    return -1