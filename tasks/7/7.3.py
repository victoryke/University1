counter = int(input())
dictionary = {}
for i in range(0,counter):
  key, value = [int(i) if i.isdigit() else i for i in input().split()]
  if key in dictionary:
    dictionary[key] += int(value)
  else:
    dictionary.__setitem__(key, value)
sortednames=sorted(dictionary.keys(), key=lambda x:x.lower())
for element in sortednames:
  print(element, dictionary[element])
