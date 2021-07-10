import time

#Date = time.localtime(time.time())


Day = time.strftime("%w")
DayName = time.strftime("%A")
TimeFull =  time.strftime('%X')
Time = TimeFull[0:5] #get the first 5 characters of TimeFull 

print('It is', DayName, ":", Day) 
print(TimeFull)
print(Time)

while 0 == 0:

    time.sleep(30)
    TimeFull =  time.strftime('%X')
    print(TimeFull)
