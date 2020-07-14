# 7 kyu
# Queue time counter
# https://www.codewars.com/kata/5b538734beb8654d6b00016d/train/python

def queue(queuers,pos):
    count = 0
    while queuers[pos] > 0:
        if pos == 0:
            pos = len(queuers) - 1
        else:
            pos -= 1
        queuers[0] -= 1
        queuers.append(queuers[0])
        queuers.pop(0)
        count += 1
    
    return count + sum([i for i in queuers if i < 0])