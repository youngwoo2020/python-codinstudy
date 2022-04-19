import math

def prime(n):
    pre = 0
    for i in range(1,int(n/2)+1):
        if n%i ==0:
            pre += 1
    if n ==1 or pre >=2:
        return False

    
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if prime(i)!=False:
            answer +=1
    return answer



print(int(math.sqrt(8)))