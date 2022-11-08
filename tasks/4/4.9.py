x = int(input())
y = int(input())
z = int(input())
counter = 0;
if(x == y):
  counter += 1
if(y == z):
  counter += 1
if(x==z):
  counter += 1
if(counter < 3):
  counter *= 2
print(counter)