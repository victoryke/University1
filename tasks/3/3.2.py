a = str( input() )
z = a.find(' ');
print(f'{a[(z+1):]} {a[:z]}')