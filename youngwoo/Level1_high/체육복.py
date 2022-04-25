n = 5
lost = [4,2]
reserve = [3,4,5]

lost.sort()
reserve.sort()

answer = 0
pre=[]
for i in lost:
    for j in reserve:
        if i==j:
            reserve.remove(j)
            lost.remove(i)
        if i-1==j or i+1==j:
            pre.append(j)
            
pre = list(set(pre))
print(pre)

if len(pre)>=len(lost):
    answer =n
else:
    answer = n-len(lost)+len(pre)
print(answer)   

