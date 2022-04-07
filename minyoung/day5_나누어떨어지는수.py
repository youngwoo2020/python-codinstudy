def solution(arr, divisor):
    ans = []

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            ans.append(arr[i])
    if not ans:
         ans.append(-1)
    return sorted(ans)
