string = str(input())
first = string.find('h')
finish = string.rfind('h')
string_middle = string[first:finish]
print(f"{string[:first+1]}{string_middle[::-1]}{string[finish:]}")
