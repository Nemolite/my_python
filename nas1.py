class Geom:
    nameclass="Базовый класс"

    def obforall(self):
        return self.nameclass

class Line(Geom):
    nameclass = "Наследник 1"

    def risun(self):
        print("Рисование линий")

class Rect(Geom):
    nameclass = "Наследник 2"

    def risun(self):
        print("Рисование прямоугольников")

l= Line()
print(l.nameclass)
l.risun()

r= Rect()
print(r.nameclass)
r.risun()

print(l.obforall())
print(r.obforall())

g= Geom()
print(g.obforall())

