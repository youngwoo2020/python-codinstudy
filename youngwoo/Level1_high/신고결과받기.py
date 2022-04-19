
from posixpath import split
from collections import Counter

k=2
id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]


answer = []
end=[]
report = list(dict.fromkeys(report))

for i in report:
    end.append(i.split(" ")[1])  

        
count = {}
for i in end:
    try: count[i] +=1
    except: count[i] = 1

fail =[]
for i in range(len(list(count.values()))):
    if list(count.values())[i]>=k:
        fail.append(list(count.keys())[i])
        
new_report =[]
for i in report:
    new_report.append(i.split(" "))

pre = []
for j in range(len(new_report)):
    for i in range(len(fail)):
        if fail[i] == new_report[j][1]:
            pre.append(new_report[j][0])
print(new_report)        
print(pre)


answer = [0 for i in range(len(id_list))]
for i in range(len(id_list)):
    for j in range(len(pre)):
        if id_list[i]==pre[j]:
            answer[i]+=1


