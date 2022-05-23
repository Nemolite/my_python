class Basa:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif(self):
        raise NotImplementedError("Функция должна быть определена")

class Plus(Basa):
    def arif(self):
        return self.x + self.y

class Minus(Basa):
    def arif(self):
        return self.x - self.y

class Poisved(Basa):
    def arif(self):
        return self.x * self.y

class Delenie(Basa):
    def arif(self):
        return self.x / self.y

pl = Plus(2,2)
print(pl.arif())

mi = Minus(4,2)
print((mi.arif()))

pr = Poisved(3,3)
print(pr.arif())

de = Delenie(9,3)
print((de.arif()))