counter = int(input())
dictionary = {}
for i in range(0,counter):
  words_list = [str(s) for s in input().split()]
  key = words_list[0]
  dictionary.__setitem__(key, words_list[1:])
counter = int(input())
keys_list = dictionary.keys()
for i in range(0, counter):
  word = str(input())
  for element in keys_list:
    if(word in dictionary[element]):
      print(element)
