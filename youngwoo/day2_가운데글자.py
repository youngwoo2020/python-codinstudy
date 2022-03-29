def solution(s):
    answer = ''
    b=0
    a= 0
    answer=""
    if len(s)%2==0:
        a = int(len(s)/2-1)
        b = int(len(s)/2)
        answer = s[a]+s[b]
    else:
        a = int(len(s)/2)
        answer = s[a]

    return answer

# def string_middle(str):
#     # 함수를 완성하세요

#     if len(str) % 2:
#         return str[len(str) // 2]
#     else:
#         return str[len(str)//2 -1 : len(str)//2 + 1 ]
