class Plus:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif(self):
        return self.x + self.y

class Minus:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif(self):
        return self.x - self.y

class Poisved:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif(self):
        return self.x * self.y

class Delenie:
    def __init__(self,x,y):
        self.x = x
        self.y = y

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