from datetime import datetime

timeA = '15:00:00'
timeB = '17:00:00'

FMT = '%H:%M:%S'

timedelta = datetime.strptime(timeB, FMT) - datetime.strptime(timeA, FMT)
print(timedelta)