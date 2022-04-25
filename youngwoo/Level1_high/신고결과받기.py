

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
answer = []

end=[]
fail =[]
report = list(dict.fromkeys(report))
count = {}
for i in range(len(report)):
    end.append(report[i].split(" ")[1])
    try: 
        count[end[i]] +=1
        if count[end[i]]>=k:
            count[end[i]]=k
            continue
    except: count[end[i]] = 1

for i in range(len(list(count.values()))):
    if list(count.values())[i]==k:
        fail.append(list(count.keys())[i])
        
print(fail)
new_report =[]
for i in report:
    new_report.append(i.split(" "))

pre = []


for j in range(len(new_report)):
    for i in range(len(fail)):
        if fail[i] == new_report[j][1]:
            pre.append(new_report[j][0])


answer = [0 for i in range(len(id_list))]
for i in range(len(id_list)):
    for j in range(len(pre)):
        if id_list[i]==pre[j]:
            answer[i]+=1
