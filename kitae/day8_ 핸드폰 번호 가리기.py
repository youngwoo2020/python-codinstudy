def solution(phone_number):
    answer = ''
    print(phone_number)
    a = len(phone_number)
    b = int(a) - 4
    c = b * "*"
    d = phone_number[b:]
    answer = c + d
    return answer
