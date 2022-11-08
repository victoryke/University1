list = [int(s) for s in input().split()]
maxval = max(list)
minval = min(list)
maxind = 0;
minind = 0;
for i in range(0, len(list)):
    if(list[i]==maxval):
        maxind = i
    if(list[i]==minval):
        minind = i
list[minind] = maxval
list[maxind] = minval
print(list)