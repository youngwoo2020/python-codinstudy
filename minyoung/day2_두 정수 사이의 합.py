def solution(a, b):
    num = 0
    if a > b:
        temp = a
        a = b
        b = temp

    for i in range(a, b+1):
        num += i

    return num
