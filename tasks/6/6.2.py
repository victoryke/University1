list = [int(s) for s in input().split()]
prev=list[0];
for element in list:
  if(element > prev):
    print(element)
  prev = element