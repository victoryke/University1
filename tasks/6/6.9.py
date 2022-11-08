string = str(input())
is2=len(string)%2
middle=len(string)//2
mediana=middle + is2
print(f"{string[mediana:]}{string[:mediana]}")
print(len(string))
