def solution(s):
    answer = True
    s = s.lower()
    n=0
    m=0
    for i in range(len(s)):
        if s[i] == "p":
            n += 1
        elif s[i] == "y":
            m +=1
    if m==n:
        answer = True
    else:
        answer = False

    return answer

#def numPY(s):
    # 함수를 완성하세요
#    return s.lower().count('p') == s.lower().count('y')