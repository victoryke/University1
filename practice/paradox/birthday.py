from random import randint


def birthday(students, iterations):
    days=365
    counter = 0
    for i in range(0,iterations):
        students_birthdays = []
        for j in range(0,students):
            birthday = randint(0,days)
            if birthday in students_birthdays:
                counter += 1
                break
            else:
                students_birthdays.append(birthday)
    result = counter/iterations*100
    return result
