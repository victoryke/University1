string = str(input())
print(string[2])
print(string[-1])
print(string[:5])
print(string[:-2])
i = 0;
for char in string:
  if (i % 2 == 0):
    print(char, end="")
  i += 1
print('')
i = 0;
for char in string:
  if (i % 2 == 1):
    print(char, end="")
  i += 1
print(string[::-1])
i = 0;
for char in string[::-1]:
  if (i % 2 == 0):
    print(char, end="")
  i += 1
