def solution(n):
    answer = 0
    a = list(str(n))
    a.sort(reverse=True)
    answer=int("".join(a))
    
    return answer
