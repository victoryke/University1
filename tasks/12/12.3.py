class Car:
    color = ""
    type = ""
    year = ""
    engineOn = False
    def __init__(self,color,type,year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        if self.engineOn:
            print("Мотор уже работает")
        else:
            print("Автомобиль заведен")
            engineOn = True
    def stop(self):
        if self.engineOn:
            print("Автомобиль заглушен")
            engineOn = False
        else:
            print("Мотор не работает")
    def set_year(self,year):
        self.year = year
    def set_type(self,type):
        self.type = type
    def set_color(self,color):
        self.color = color
nissan = Car("black", "sedan", "2007")
nissan.start()
nissan.start()
nissan.stop()
nissan.stop()
nissan.set_year("2008")
nissan.set_type("universal")
nissan.set_color("white")
print(nissan.color,nissan.type,nissan.year)
