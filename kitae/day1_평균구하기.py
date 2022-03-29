def solution(arr):
    answer = 0 
    for i in arr:
        answer=answer+i
    avg = answer/len(arr)
    return avg
