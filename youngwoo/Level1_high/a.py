

from collections import defaultdict


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
report = list(dict.fromkeys(report))
count = {}
end =[]

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