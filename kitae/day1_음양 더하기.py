import numpy as np
d = 0
c = 0
def solution(absolutes, signs):
    answer = 123456789
    a = np.where(np.array(signs) == True)[0]
    b = np.where(np.array(signs) == False)[0]

    for i in a:
        global c
        c += absolutes[i]
    for j in b:
        global d
        d += absolutes[j]
    answer = c - d
    return answer
