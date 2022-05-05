class Integer:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__:{self.name} = {value}")
        instance.__dict__[self.name] = value

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls,coord):
        if coord != int:
            raise TypeError('Координата должна быть целым числом')



coord = Point3D(2,3,4)
print(coord.__dict__)