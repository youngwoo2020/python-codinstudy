def solution(n):
    answer = 0
    first =""
    if n<3:
        first+=str(n)
    while n>=3:
        first+=str(int(n%3))
        n /=3
        if n<3 :
            first+=str(int(n))
    first = str(int(first))
    first=first[::-1]
    for i in range(len(first)):
        answer+=(3**i)*int(first[i])
    return answer
    
    
