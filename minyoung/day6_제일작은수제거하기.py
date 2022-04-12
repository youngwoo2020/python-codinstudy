def solution(arr):
    arr.remove(min(arr))

    if not list(arr):
        return [-1]
    else:
        return arr
