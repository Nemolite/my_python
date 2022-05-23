class Point:
    __slots__ = ('x','y')
    z = 23
    def __init__(self,x,y):
        self.x = x
        self.y = y

ds = Point(3,4)
print(ds.z)

print(ds.__sizeof__())
