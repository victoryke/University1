import re
file = open("input.txt", mode="r", encoding="UTF-8")
text = file.readlines()
pattern = r"(?:^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w) (\d+:\d+:\d+)"
data = []
for line in text:
    if re.findall(pattern,line):
        data.append(re.findall(pattern,line))
file.close()
file = open("output.txt", mode="w", encoding="UTF-8")
for row in data:
    file.write(f"[{row[0][3]}] - Поезд №{row[0][0]} {row[0][1]} {row[0][2]} \n")
file.close()
