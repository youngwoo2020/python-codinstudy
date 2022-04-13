def solution(x):
    answer = True
    a=0
    for i in range(len(str(x))):
        a += int(str(x)[i:i+1])   
    print(a)
    if x%a==0:
        answer = True
    else:
        answer = False
    return answer
