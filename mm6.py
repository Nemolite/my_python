#Магические методы сравнения
class Clock:
    __DAY = 86400 # Число секунд в одном дне

    def __init__(self,sec:int):
        if not isinstance(sec, int):
            raise TypeError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def __eq__(self, other): # автоматический сработает маг метод __ne__
        if not isinstance(other,(int,Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other,int) else other.sec
        return self.sec ==sc

    def __lt__(self, other):
        if not isinstance(other,(int,Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other,int) else other.sec
        return self.sec < sc

obj1 = Clock(1000)
print(obj1.__dict__)

obj2 = Clock(1000)
print(obj2.__dict__)

print(obj1==obj2)

print(obj1<obj2)