def solution(nums):
    answer = 0
    n = int(len(nums)/2)
    if len(list(set(nums)))>=len(nums)/2:
        answer = n
    else:
        answer = len(list(set(nums)))
    return answer