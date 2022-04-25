

def solution(n, arr1, arr2):
    
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