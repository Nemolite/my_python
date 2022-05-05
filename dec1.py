class Point3D:
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def verify_coord(cls,coord):
        if coord != int:
            raise TypeError('Координата должна быть целым числом')


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, x):
        self._z = z