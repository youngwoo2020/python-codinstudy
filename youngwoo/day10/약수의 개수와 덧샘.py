def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        pre = 0
        for j in range(1,i+1):
            if i%j==0:
                pre += 1
        if pre%2==0:
            answer +=j
        else:
            answer -= j
    return answer