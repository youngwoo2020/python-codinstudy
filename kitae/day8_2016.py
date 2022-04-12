from datetime import datetime
def solution(a, b):
    answer = ''
    date = '2016' + '-' + str(a) + '-' + str(b+1)
    datetime_data = datetime.strptime(date, '%Y-%m-%d')
    print(datetime_data.weekday())
    dateDict = {0: 'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
    answer = dateDict[datetime_data.weekday()]
    return answer
