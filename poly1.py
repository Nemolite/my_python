class Plus:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif_plus(self):
        return self.x + self.y

class Minus:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif_minus(self):
        return self.x - self.y

class Poisved:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif_prois(self):
        return self.x * self.y

class Delenie:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arif_dele(self):
        return self.x / self.y

pl = Plus(2,2)
print(pl.arif_plus())

mi = Minus(4,2)
print((mi.arif_minus()))

pr = Poisved(3,3)
print(pr.arif_prois())

de = Delenie(9,3)
print((de.arif_dele()))
