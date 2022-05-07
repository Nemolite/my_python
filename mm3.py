class Clock:
    __DAY = 86400

    def __init__(self, second: int):
        if not isinstance(second, int):
            raise TypeError("Секунды должны быть целыми числами")
        self.second = second % self.__DAY
        #print(self.second)

    def get_time(self):
        s = self.second % 60
        #print(s)
        m = (self.second // 60) % 60
        #print(m)
        h = (self.second // 3600 ) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls,x):
        return str(x).rjust(2,"0")

    def __add__(self, other):
        return Clock(self.second + other)

c = Clock(1000)
print(c.__dict__)
print(c.get_time())
c.second = c.second + 100
print(c.get_time())

c = c + 200
print(c.get_time())


