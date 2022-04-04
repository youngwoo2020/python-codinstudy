def solution(n):
    answer = 0
    abc = []
    a = f'{n}'
    b = len(a)
    for i in range(1,b+1):
        answer += int(a[i-1:i])
    return answer
