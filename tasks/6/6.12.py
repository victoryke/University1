string = str(input())
start = string.find('h')
finish = string.rfind('h')
i = 0
for i in range(0, len(string)-1):
  if(i!=start) and (i!=finish) and (string[i] == 'h'):
    print('H', end="")
  else:
    print(string[i], end='')
