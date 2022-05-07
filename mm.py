class Cat:
    def __init__(self,name):
        self.name = name

    def __repr__(self): # вывод отладочной информации
        return f"{self.__class__}: {self.name}"

    def __str__(self): # вывод информации для пользователя
        return f"{self.name}"
