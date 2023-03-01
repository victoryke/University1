class Student:
    def __init__(self,name,age = 20,groupNumber = "10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getgroupNumber(self):
        return self.groupNumber
    def setNameAge (self,name,age):
        self.name = name
        self.age = age
        return self.name,self.age
    def setgroupNumber(self,groupNumber):
        self.groupNumber = groupNumber
        return self.groupNumber
Ivan = Student("Иван",20,"11Б")
Masha = Student("Маша",19,"9Б")
Vika = Student("Вика",21,"10А")
Misha = Student("Миша",18,"11Б")
Alisa = Student("Алиса",20,"03Д")
print(Ivan.getName(),Ivan.getAge(),Ivan.getgroupNumber())
print(Masha.getName(),Masha.getAge(),Masha.getgroupNumber())
print(Vika.getName(),Vika.getAge(),Vika.getgroupNumber())
print(Misha.getName(),Misha.getAge(),Misha.getgroupNumber())
print(Alisa.getName(),Alisa.getAge(),Alisa.getgroupNumber())