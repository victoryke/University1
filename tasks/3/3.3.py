s = str(input())
first = s.find('f')
last = s.rfind('f')
if (first == last) and (first == -1):
  print(f"{-1}")
elif (first == last) and (first != -1):
  print(f"{first}")
else :
  print(f'{first} {last}')