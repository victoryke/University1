counter = int(input())
dictionary = {}
for i in range(0,counter):
  words_list = [str(s) for s in input().split()]
  for element in words_list:
    if element in dictionary:
      dictionary[element] += 1
    else:
      dictionary.__setitem__(element, 1)
sortednames=sorted(dictionary.keys(), key=lambda x:x.lower())
print(max(dictionary, key=dictionary.get), dictionary.get(max(dictionary, key=dictionary.get)))
