num = int(input())
nod = 1
counter = 2
while (nod == 1):
  if(num % counter == 0):
    nod = counter
  else:
    counter += 1
print(nod)