from datetime import datetime,timedelta

birth_day=input("Please Enter your Birthday @ Format of 'DD/MM/YYYY' :")

Birth_Date = datetime.strptime(birth_day,'%d/%m/%Y')

print("Day of your Birth Day is :"+ str(Birth_Date.day))
print("Month of your Birth Day is :"+ str(Birth_Date.month))
print("Year of your Birth Day is :"+ str(Birth_Date.year))
no_of_days=timedelta(days=1)
print("Date before your Birthday is :" + str((Birth_Date-no_of_days).day) +"th  "+ str( Birth_Date-no_of_days )   )
print("The Next Date of your Birthday is :" + str((Birth_Date+no_of_days).day) +"th  "+ str(Birth_Date+no_of_days)  )
