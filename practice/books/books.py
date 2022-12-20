import csv
def read_file():
    with open("books.csv") as csvfile:
        file = csv.reader(csvfile, delimiter="|")
        data = []
        for row in file:
            data.append(row)
    return data[1:]

def search(row, key_word):
    flag = False
    for element in row:
        string = str(element)
        string = string.lower()
        key_word = key_word.lower()
        if (string.find(key_word) != -1):
            flag = True
            break
        else:
            flag = False
    return flag
def get_books(key_word):
    data = read_file()
    returnable = []
    for row in data:
        if search(row, key_word):
            returnable.append(row)
    return returnable


def get_totals_2(list, limiter, counter):
    returnable = []
    for row in list:
        number = (int(row[3]) * int(row[4]))
        if (number < limiter):
            number += counter
        data = tuple([str(row[0]), str(number)])
        returnable.append(data)
    return returnable