def solution(s,n):
    answer = ""
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Alpha =[]
    for i in alpha:
        Alpha.append(i.capitalize())
    


    for j in range(len(s)):
        for i in range(len(alpha)):
            if s[j]==alpha[i]:
                if i+n<len(alpha):
                    answer += alpha[i+n]
                else:
                    answer+= alpha[i+n-len(alpha)]
            elif s[j]==Alpha[i]:
                if i+n<len(alpha):
                    answer += Alpha[i+n]
                else:
                    answer+= Alpha[i+n-len(Alpha)]
        if s[j]==" ":
            answer += " "
    return(answer)