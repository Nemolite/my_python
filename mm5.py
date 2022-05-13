class Clock:
    __DAY = 86400

    def __init__(self, second: int):
        if not isinstance(second, int):
            raise TypeError("Секунды должны быть целыми числами")
        self.second = second % self.__DAY

    def get_time(self):
        s = self.second % 60
        m = (self.second // 60) % 60
        h = (self.second // 3600 ) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls,x):
        return str(x).rjust(2,"0")

    def __add__(self, other):
        if not isinstance(other,(int,Clock)):
            raise ArithmeticError("Правый операнд должент быть int или Clock")
        sc = other
        if isinstance(other,Clock):
            sc = other.second
        return Clock(self.second + sc)
    def __radd__(self, other):
        return  self + other
    def __iadd__(self, other):
        if not isinstance(other, (int,Clock)):
            sc = other.second
        self.second+=sc
        return self

obj  = Clock(1000)
obj = 100 + obj
print(obj.__dict__)
print(obj.get_time())



