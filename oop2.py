###################
# Магические методы

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def __del__(self):
        print('Объект удален')

pn1 = Point(2,3)
pn2 = Point(3,4)

print(Point.__dict__)
print('##################')
print(pn1.__dict__)
print('##################')
print(pn2.__dict__)
del pn1

