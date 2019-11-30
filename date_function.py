from  datetime import datetime, timedelta
diff_time=timedelta(hours=1)
print(datetime.now()+diff_time)

one_day=timedelta(days=1)
yesterday=datetime.now()-one_day
tomorrow = datetime.now()+one_day
print("Yesterday date is :"+ str(yesterday))
print("Today is          :" + str(datetime.now()))
print("Tomorrow date is  :"+ str(tomorrow))
one_week = timedelta(weeks=1)
print(datetime.now()-one_week)