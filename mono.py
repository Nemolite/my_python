class Mymono:
    __my_attrs = {
        'name':'Sergey',
        'data': {},
        'id':1
    }
    def __init__(self):
        self.__dict__ = self.__my_attrs

o1 = Mymono()
o2 = Mymono()

o1.exe = 23
print(o2.exe)
