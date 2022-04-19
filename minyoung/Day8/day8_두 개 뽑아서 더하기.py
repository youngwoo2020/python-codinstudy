def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                result.append(numbers[i] + numbers[j])
                
    return sorted(set(result))
