numbers = {}
def get_num():
    number=str(input())
    if (number[0] == '+') and (number[1] == '7') and (len(number) == 12):
        return number
    elif (number[0] == "8") and (len(number) == 11):
        ch_number = "+7" + number[1:]
        return ch_number
    elif (len(number) == 10):
        ch_number = "+7" + number
        return ch_number
    else:
        return False
def get_name():
    name = str(input("введите имя контакта"))
    name=name.title().strip()
    return name
def get_full_number():
    name = get_name()
    number = get_num()
    if (number):
        numbers[name] = number
    else:
        print("неправильный номер")
def change_num():
    name = get_name()
    number = get_num()
    if name in numbers.keys()
        numbers[name]=number
    else:
        print("неправильный номер")
def delete_num():
    name = get_name()
    if (name in numbers.keys()):
        del numbers[name]
    else:
        print("не существует имени")
while True:
    print("выбери действие: 0-добавить,1-изменить, 3-удалить, 2-показать")
    step = str(input('Какое действие выберете'))
    if(step == "0"):get_full_number()
    elif(step == "1"):change_num()
    elif (step == '2'):print(numbers)
    elif (step == "3"):delete_num()