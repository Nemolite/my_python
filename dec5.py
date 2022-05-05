class Readparam:
    def __set_name__(self, owner, name):
        self.name = "_x"
    def __get__(self, instance, owner):
        return getattr(instance,self.name)

class Integer:

    @classmethod
    def verify_coord(cls,coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        #return instance.__dict__[self.name]
        return getattr(instance,self.name)

    def __set__(self, instance, value):
        #print(f"__set__:{self.name} = {value}")
        self.verify_coord(value)
        #instance.__dict__[self.name] = value
        setattr(instance,self.name,value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = Readparam()

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

coord = Point3D(2,3,4)
print(coord.__dict__,coord.xr)