
# def binary(a):
#     component = ""
#     while a>0:
#         component += str(a%2)
#         a = int(a/2)
#         if a<2:
#             component+=str(a)
#             break
#     if len(component)<n:
#         component +=(n-len(component))*"0"
#     return (component[::-1])

# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         real = ""
#         for j in range(n):
#             if binary(arr1[i])[j]=="0" and binary(arr2[i])[j]=="0":
#                 real += " "
#             else:
#                 real += "#"
#         answer.append(real)
#     return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 =[30, 1, 21, 17, 28]

def binary(n, arr):
    for i in arr:
        c = bin(i)
        c = c.replace('b','0')
        c= list(c[-n:])
        print(c[0])


(binary(n, arr1))


# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         real = ""
#         for j in range(n):
#             if binary(n,arr1[i])[j]=="0" and binary(n,arr2[i])[j]=="0":
#                 real += " "
#             else:
#                 real += "#"
#         answer.append(real)
#     return answer

    
        


# print(solution(n, arr1, arr2))