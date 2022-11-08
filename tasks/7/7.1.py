listz = [str(s) for s in input().split()]
checked = []
for element in listz:
  counter = 0
  for s in checked:
    if (element==s):
      counter +=1
  checked.append(element)
  print(counter)
