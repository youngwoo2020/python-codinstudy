def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return answer
        if num % 2 == 0:
            num = int(num/2)
            answer += 1
        else:
            num = int(num * 3 + 1)
            answer += 1

    return -1
