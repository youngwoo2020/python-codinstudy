y = 0
def solution(x, n):
    answer = []
    for i in range(n):
        global y
        y = y + x
        answer.append(y)

    return answer
