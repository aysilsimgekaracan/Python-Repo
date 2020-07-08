# 6 kyu
# The Supermarket Queue
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
    queque = {}
    i = 0
    
    if len(customers) == 0:
        return 0
    elif len(customers) < n:
        return max(customers)
    
    while  i < n:
        queque[i] = customers[i]
        i += 1
    while i < len(customers) :
        value = min(queque.values())
        key = get_key(value, queque)
        queque[key] = queque[key] + customers[i]
        i += 1

    return max(queque.values())

def get_key(val, dict):
    for key, value in dict.items(): 
        if val == value: 
            return key 