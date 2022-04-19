

import re
s= "0one4seven7eight5"

answer =0

strs=["zero", "one","two", "three", "four","five", "six", "seven", "eight", "nine"]
num ={}

def switch(s, strs):
    for i in range(len(strs)):
        num[strs[i]] = i
    return num.get(s)
pre=""
for i in range(len(s)):
    if (s[i]).isdigit()==True:
        print(s.split(s[i])[0],s[i],s.split(s[i])[1])

print("--------------")
for i in strs:
    if len(s.split(i))==2:
        print(s.split(i)[0],switch(i,strs),s.split(i)[1])

