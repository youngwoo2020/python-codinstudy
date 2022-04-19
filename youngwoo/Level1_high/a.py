
def binary(a):
    component = ""
    while a>0:
        component += str(a%2)
        a = int(a/2)
        if a<2:
            component+=str(a)
            break
    if len(component)<n:
        component +=(n-len(component))*"0"
    return (component[::-1])

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        real = ""
        for j in range(n):
            if binary(arr1[i])[j]=="0" and binary(arr2[i])[j]=="0":
                real += " "
            else:
                real += "#"
        answer.append(real)
    return answer

n = 5
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 =[27 ,56, 19, 14, 14, 10]    
print(solution(n, arr1, arr2))