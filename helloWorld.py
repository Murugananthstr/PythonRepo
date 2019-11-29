from datetime import datetime, timedelta
print('Hello World')
# first_name = input('What is your First Name: ')
# second_name = input('What is your Second Name: ')

# name = first_name + ' ' + second_name

# print(name.count(' '))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print ('Other way of Formatting')

# print('Hello, '+first_name +' ' + second_name)
# print('Hello, {} {}'.format(first_name,second_name))
# print('Hello, {0} {1}'.format(first_name,second_name))
# print ('Below format is only available in version 3 and above')
# print(f'Hello, {first_name} { second_name}')
diff_time=timedelta(hours=1)
print(datetime.now()+diff_time)

one_day=timedelta(days=1)
print(datetime.now()-one_day)

one_week = timedelta(weeks=1)
print(datetime.now()-one_week)


