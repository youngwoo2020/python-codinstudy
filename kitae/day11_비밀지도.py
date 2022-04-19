def solution(n, arr1, arr2):
    answer = []
    arr11 = []
    arr22 = []
    
    for i in arr1:
        a=bin(i)
        a = a[-n:]
        a = a.replace("b","0")
        if len(a) != n:
            a = a.rjust(n, "0")

        arr11.append(a)
            
    for i in arr2:
        a=bin(i)
        a = a[-n:]
        a = a.replace("b","0")
        if len(a) != n:
            a = a.rjust(n, "0")

        arr22.append(a)    
    print(arr11)
    print(arr22)
    
    for p in range(n):
        ee = ""
        for q in range(n):
            if arr11[p][q] == "1" or arr22[p][q] == "1":
                ee += '#'
            else:
                ee += " "
        answer.append(ee)
    return answer
