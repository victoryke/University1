counter = int(input())
dictionary = {}
for i in range(0,counter):
  words_list = [str(s) for s in input().split()]
  for element in words_list:
    if element in dictionary:
      dictionary[element] += 1
    else:
      dictionary.__setitem__(element, 1)
sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
for item in sorted_dict:
  print(item)
