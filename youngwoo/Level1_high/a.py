

k=2
id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k):
    answer = []
    count = {}
    report = list(dict.fromkeys(report))
    for i in report:
        print(i.split(" ")[1])
        try: count[i.split(" ")[1]]+=1
        except : count[i.split(" ")[1]]=1
        

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



    answer = [0 for i in range(len(id_list))]
    for i in range(len(id_list)):
        for j in range(len(pre)):
            if id_list[i]==pre[j]:
                answer[i]+=1
    return answer