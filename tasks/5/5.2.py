num = int(input())
degree = 0;
powered_number = pow(2, degree)
while (powered_number < num):
  degree += 1
  powered_number = pow(2, degree)
  if(powered_number>num):
    degree -=1
powered_number = pow(2, degree)
print(f'{degree} {powered_number}')