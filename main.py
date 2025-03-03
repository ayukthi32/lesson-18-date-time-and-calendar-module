#activity1

from datetime import date , time , datetime

today = date.today()
now = datetime.now()

print("Todays date is" , today)
print("current date and time is:" , now)

print("Datetime components" , today.year , today.month , today.day)