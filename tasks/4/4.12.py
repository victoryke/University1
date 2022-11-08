x = int(input())
y = int(input())
if (x == 1) or (x == 3) or (x == 5) or (x == 7) or (x == 8) or (x == 10) or (x == 12):
    days = 31
elif (x == 2):
    days = 28
else:
    days = 30
day = y + 1
if (day > days):
    month = x + 1
    day = 1
else:
    month = x
if (month > 12):
    year = 2023
    month = 1
else:
    year = 2022
print(f'{day}-{month}-{year}')
