list = [int(s) for s in input().split()]
for i in range(1, len(list), 2):
    print(f'{list[i]} {list[i-1]} ', end="")
if (len(list) % 2 == 1):
    print(list[len(list)-1])