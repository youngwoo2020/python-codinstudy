def solution(n):
    answer = 0
    if n<10:
        answer += n
    while n>=10:
        answer += int(n%10)
        n=int(n/10)
        if n<10:
            answer += n
            break
    return answer

#def sum_digit(number):
#    return sum([int(i) for i in str(number)])

#존나이해가안간다