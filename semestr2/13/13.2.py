class SuperStr(str):
    def __init__(self, string):
        self.string = string
    def is_repeatance(self, string):
        if not (isinstance(string, str)):
            return False
        while True:
            if(len(string)>len(self.string)):
                return False
            elif(len(string)<len(self.string)):
                string = string + string
                continue
            elif(len(string)==len(self.string) and (string == self.string)):
                return True
            else:
                break
    def is_palindrom(self):
        if(self.string == self.string[::-1]):
            return True
        else:
            return False

s = SuperStr("123123123123")
print(s.is_repeatance("123")) # True
print(s.is_repeatance("123123")) # True
print(s.is_repeatance("123123123123")) # True
print(s.is_repeatance("12312")) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (строка)
print(int(s)) # 123123123123 (целое число)
print(s + "qwe") # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom()) # True