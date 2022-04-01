def solution(s):
    answer = ''
    a = len(s)
    b=int(a/2+0.5)
    if a%2 == 0:
        answer = s[b-1:b+1]
    else:
        answer = s[b-1]
    return answer
