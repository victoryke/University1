x = int(input())
y = int(input())
dist = x;
day = 1
while (dist < y):
  dist += (dist / 10)
  day += 1
print(day)