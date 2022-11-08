num = int(input())
counter = 0
while(num != 0):
    num_prev = num
    num = int(input())
    if(num>num_prev):
      counter += 1
print(counter)