from cmath import phase


new_id = "...!@BaT#*..y.abcdefghijklm"



#1단계
phase1 = new_id.lower()

#2단계
phase2=""
for i in phase1:
    if i.isalpha()==True or i.isnumeric()==True or i=="-" or i=="_" or i==".":
        phase2 += i

#3단계
phase3=[]

print(phase2.count("."))


print(phase2)
for i in range(len(phase2)-1):
    if phase2[i]=="." and phase2[i+1]==".":
        phase3.append(i)
        
print(phase3)
