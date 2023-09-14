from datetime import datetime 

create_date = datetime(2023,9,24)

def hora_new (date):
    print(date.day)


hora_new(create_date)





from datetime import time

create_time = time(5,50,24)
print(create_time.minute)



from datetime import timedelta

my_timedelta = timedelta(8, weeks=1, hours=13)
my_timedelta2 = timedelta(16, weeks=2, hours=12)

print(my_timedelta + my_timedelta2)



