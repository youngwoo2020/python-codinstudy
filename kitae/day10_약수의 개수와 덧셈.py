def solution(left, right):
    answer = 0

    for j in range(left, right+1):
        a = 0
        for i in range(1, j+1):
            if j % i == 0:
                a += 1
        if a % 2 == 0:
            print(j)
            answer += j
        else:
            answer -= j
    
    return answer
