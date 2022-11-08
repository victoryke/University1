num1 = int(input())
counter = 0
mini_counter = 1
while (num1 != 0):
    num0=num1
    num1 = int(input())
if(num1 == num0):
    mini_counter +=1
else:
    mini_counter = 1
if(mini_counter>counter):
    counter=mini_counter;
print(counter)