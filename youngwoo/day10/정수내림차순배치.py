def solution(n):
    n = str(n)
    answer =""
    pre = []
    for i in range(len(n)):
        pre.append(int(n[i]))
    pre.sort()
    pre.reverse()
    for i in range(len(pre)):
        answer += str(pre[i])
    answer = int(answer)
    return answer