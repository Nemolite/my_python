class Point:
    def __init__(self,*args):
        self.__coord = args

    def __len__(self):
        return len(self.__coord)

    def __abs__(self):
        return list(map(abs, self.__coord))

p = Point(2,-4,30)
print(len(p))
print(abs(p))
