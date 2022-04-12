
month = 5
day = 24
answer = ""
week =["FRI","SAT","SUN","MON","TUE","WED","THU"]
month_array = [31,28,31,30,31,30,31,31,30,31,30,31]
date = 0

for i in range(2,month+1):
    date+=month_array[month-i]

date += day
print(date)
print(date%7)

for i in range(len(week)):
    if date%7 == i:
        answer = week[i]


print(answer)