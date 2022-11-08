counter = int(input())
dictionary = {}
for i in range(0,counter):
  words_list = [str(s) for s in input().split()]
  key = words_list[0]
  dictionary.__setitem__(key, words_list[1:])
counter = int(input())
for i in range(0, counter):
  words_list = [str(s) for s in input().split()]
  motion = words_list[0][0].upper()
  if(motion in dictionary[words_list[1]]):
    print("OK")
  else:
    print("DENIED")
