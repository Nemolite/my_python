class Point:
    a = 11  
    b = 12
    _x = 13
    _y = 14
    __pz = 15
    __pv = 16

    @classmethod
    def get_param(cls):
        return (cls.__pz, cls.__pv)
    @staticmethod
    def experem(k,l):
        print("Пример работы статического метода")
        return k + l

obj = Point()
print(obj.a)
print(obj.b)
print(obj._x)
print(obj._y)
#print(obj.__pz)`
#print(obj.__pv)
print(obj.get_param())
res1 = obj.experem(3,3)
res2 = Point.experem(6,7)
print(res1,res2)
