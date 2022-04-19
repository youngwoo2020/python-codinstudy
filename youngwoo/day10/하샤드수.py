def solution(x):
    answer = False

    x = str(x)
    pre =0
    for i in range(len(x)):
        pre+=int(x[i])

    if int(x)%pre==0:
        answer = True
    return answer