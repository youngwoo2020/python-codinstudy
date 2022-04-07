import math

def solution(n):
    sq = int(math.sqrt(n))
    if sq ** 2 == n:
        return (sq + 1) ** 2
    else:
        return -1
