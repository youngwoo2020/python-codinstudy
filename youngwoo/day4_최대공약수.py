def solution(n, m):
    answer = []
    x=0
    y=0

    for i in range(1,m+1):
        if m%i==0 and n%i==0:
            x=i
    y = int((n/x)*(m/x)*x)        


    answer = [x,y] 
    return answer