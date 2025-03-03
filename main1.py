#activity2
import random
import time

def getRandomDate (startDate , endDate):
    print("Printing random dates between", startDate , "and" , endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate , dateFormat))
    endTime = time.mktime(time.strptime(endDate , dateFormat))

    randomtime = startTime + randomGenerator * (endTime - startTime)
    randomdate = time.strftime (dateFormat , time.localtime(randomtime))

    return randomdate
print("randomdate" , getRandomDate("1/1/2013" , "2/3/2014"))

    
    