z = int(input())
hun = z // 100;
z = z % 100;
dig = z // 10;
num = z % 10;
if (hun<dig) and (dig<num):
    print("да")
else :
    print("нет")