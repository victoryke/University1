import re
file = open("kutlak.txt", mode="r", encoding="UTF-8")
text = file.readlines()
pattern = r"(?:^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w) (\d+:\d+:\d+)"
for line in text:
    print(re.match(pattern,line))

