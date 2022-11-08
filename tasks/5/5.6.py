num = int(input())
n = 1
n1 = 1
n2 = 1
counter = 2
while (n < num):
    n1 = n2
    n2 = n
    n=n1+n2
    counter +=1

if(n != num):
    print(-1)
else:
    print(counter)
