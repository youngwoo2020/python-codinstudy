
answer = ""

m =3
n = 5
def solution(n,m):
    answer = ""
    for i in range(m):
        answer =((("*"*n)+"\n")*(m-1) + ("*"*n))
    return answer

print(solution(n,m))