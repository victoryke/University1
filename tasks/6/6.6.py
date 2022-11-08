list1 = [int(s) for s in input().split()]
list2 = [int(s) for s in input().split()]
for element1 in list1:
    for element2 in list2:
        if(element1 == element2):
            print(f'{element1} ', end="")