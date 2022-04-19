


s= "one4seveneight"
answer =0

strs=["zero", "one","two", "three", "four","five", "six", "seven", "eight", "nine"]
num ={}

def switch(s, strs):
    for i in range(len(strs)):
        num[strs[i]] = i
    return num.get(s)

for i in strs:
    if len(s.split(i))==2:
        print(switch(i,strs))