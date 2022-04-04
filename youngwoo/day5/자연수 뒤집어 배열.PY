def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(int(n[i]))

    return answer[::-1]


#def digit_reverse(n):
#    return [int(i) for i in str(n)][::-1]