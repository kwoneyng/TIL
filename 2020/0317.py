import datetime

cur = datetime.datetime.now()
print(cur)
def month_day(year, month):
    if month <= 6:
        if month % 2 == 1:
            return days[3]
        elif month != 2: 
            return days[2]
        elif (year%4 == 0) and (year%100 != 0) or (year%400) == 0:
            return days[1]
        else:
            return days[0]
days = [28,29,30,31]

print(month_day(cur.year,cur.month),'days for', cur.year, '-', cur.month)
