list_unchecked = [int(s) for s in input().split()]
list_checked = []

for unchecked in list_unchecked:
  flag = False
  for checked in list_checked:
    if (checked == unchecked):
      flag = True
      break
    else:
      continue
  if not flag:
    print("НЕТ")
    list_checked.append(unchecked)
  else:
    print("ДА")
