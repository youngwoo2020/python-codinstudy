def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer
