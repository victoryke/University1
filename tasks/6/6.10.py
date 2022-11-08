string = str(input())
first = string.find('h')
finish = string.rfind('h')
print(f"{string[:first]}{string[finish+1:]}")
