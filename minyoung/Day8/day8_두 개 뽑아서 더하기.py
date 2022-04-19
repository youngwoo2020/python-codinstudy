def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            k = numbers[i] + numbers[j]

            if i != j and k not in result:
                result.append(k)

    return sorted(result)
