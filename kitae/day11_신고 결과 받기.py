from collections import OrderedDict

def solution(id_list, report, k):

    a = [i.split(" ") for i in list(dict.fromkeys(report))]
    b = [a[i][0] for i in range(len(a))]
    c = [a[i][1] for i in range(len(a))]
    d = [i for i in id_list if c.count(i) >= k]
    e = [b[j] for i in d for j in range(len(a)) if i == c[j]]
    answer = [e.count(i) for i in id_list]

    return answer
