a = int(input())
hundreds = a//100;
a = a % 100;
digits = a/10;
numbers = a % 10;
summa = int(hundreds + digits + numbers);
print(f'{summa}')