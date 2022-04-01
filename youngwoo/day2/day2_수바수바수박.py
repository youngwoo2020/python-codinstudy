def solution(n):
    answer = ''
    for i in range(int(n/2)):
        answer += answer.join("수")
        answer += answer.join("박")
    if n%2==1:
        answer += answer.join("수")    
    return answer
# def water_melon(n):
#     s = "수박" * n
#     return s[:n]
