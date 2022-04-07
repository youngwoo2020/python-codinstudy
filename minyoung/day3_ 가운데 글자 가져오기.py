def solution(s):
    if len(s) % 2 == 1:
        return s[int(len(s) / 2)]
    else:
        length = int(len(s) / 2) - 1
        return s[length:length+2]
