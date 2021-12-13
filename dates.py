import datetime

my_day = datetime.datetime.now()
my_day2 = datetime.date.today()



print(my_day)
print(f"Formato LATAM: {my_day2.strftime('%d/%m/%Y')}")
print(f"Formato USA: {my_day2.strftime('%m/%d/%Y')}")
print(f'Year: {my_day2.year}')
print(f'Month: {my_day2.month}')
print(f'Day: {my_day2.day}')

