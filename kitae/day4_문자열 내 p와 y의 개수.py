def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    print(s)
    a = s.count('P')
    b = s.count('p')
    c = s.count('Y')
    d = s.count('y')
    e = a + b
    f = c + d
    if e == f:
        answer = True
    else:
        answer = False
    return answer
