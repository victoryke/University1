counter = int(input())
dictionary = {}
for i in range(0,counter):
  value_array = input().split()
  value = value_array[0]
  key = value_array[1]
  dictionary.__setitem__(key, value)
word = str(input())
print(dictionary[word])
