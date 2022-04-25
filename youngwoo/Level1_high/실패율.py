n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	
stages.sort()
fail = {}


for i in stages:
    try:
        fail[i]+=1
    except:
        fail[i]=1

print(fail)
