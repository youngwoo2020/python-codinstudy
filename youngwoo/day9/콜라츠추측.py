def solution(n):
    answer = 0
    while n>1 and answer<500:
        if n%2==0:
            n /= 2
            answer += 1
        elif n%2==1:
            n = n*3+1
            answer +=1
    if answer>=500:
        answer = -1
    return answer