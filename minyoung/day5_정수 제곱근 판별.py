import math

def solution(n):
    sq = int(math.sqrt(n))
    if sq * sq == n:
        return (sq + 1) * (sq + 1)
    else:
        return -1
