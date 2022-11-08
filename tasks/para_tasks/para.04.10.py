numbers = {}
def check_number(number):
        if (number[0] == '+') and (number[1] == '7') and (len(number) == 12):
            return number
        elif (number[0] == "8") and (len(number) == 11):
            checked_number = "+7" + number[1:]
            return checked_number
        elif (len(number) == 10):
            checked_number = "+7" + number
            return checked_number
        else:
            return False
print("You can add, change, delete, end, sort, show")
while True:
    move = str(input('what type of move you wanna choose?'))
    if (move == "add"):
        name = str(input("Type name")).title()
        number = str(input("Type_number"))
        if check_number(number):
            number = check_number(number)
            numbers[name] = number
        else:
            print("WRONG NUMERO")

    elif (move == 'change'):
        name = str(input("Type name")).title()
        number = str(input("Type_number"))
        if check_number(number):
            number = check_number(number)
            numbers[name] = number
        else:
            print("WRONG NUMERO")
    elif (move == "delete"):
        name = str(input()).title()
        if (name in numbers.keys()):
            del numbers[name]
    elif (move == "show"):
        print(numbers)
    elif (move == 'sort'):
        numbers = sorted(numbers)
    elif (move == "end"):
        break
print(numbers)