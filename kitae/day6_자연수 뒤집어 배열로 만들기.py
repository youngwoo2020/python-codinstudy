def solution(n):
    answer = []
    a = str(n)
    for i in range(len(a)):
        answer.append(a[i])
    answer=list(map(int, answer))
    answer.reverse()
    return answer
