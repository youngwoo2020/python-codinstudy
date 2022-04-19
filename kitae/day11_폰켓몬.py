def solution(nums):
    answer = 0
    a = int(len(nums)/2)
    b = set(nums)
    if int(len(b)) > a:
        answer = a
    else:
        answer = len(b)
    return answer
