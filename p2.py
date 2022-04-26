class Prop2:
    def __init__(self,inner):
        self.__inner = inner

    def set_inner(self,inner):
        self.__inner = inner

    def get_inner(self):
        return self.__inner

    inner = property()
    inner = inner.setter(set_inner)
    inner = inner.getter(get_inner)


a = Prop2
a.inner = 22
print(a.inner)
