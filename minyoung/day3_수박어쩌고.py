def solution(n):
    str = ''
    for i in range(n):
        if i % 2 == 0:
            str = str + '수'
        else:
            str = str + '박'
    return str
