def solution(n):
    remain = 0
    answer = 0
    while n >= 10:
        remain = n % 10
        n = int(n / 10)
        answer += remain
        
    answer += n
    return answer
