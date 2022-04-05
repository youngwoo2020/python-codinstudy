def solution(arr):
    answer = []
    if len(arr)>1:
        del arr[arr.index(min(arr))]
    else:
        arr = []
        arr.append(-1)

    return arr
