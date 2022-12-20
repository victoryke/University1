
def sum_digit(digit):
    digit=str(digit)
    sum=0
    if digit.isdigit():
        digit=int(digit)
        while digit > 0:
            sum += digit % 10
            digit = digit // 10
        print(sum)
    else:
        print("Некоректный тип данных")
sum_digit("ikj;'jl")



    else:
        print("Некоректный тип данных")