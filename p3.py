class Prop3:
    def __init__(self,inner):
        self.__inner = inner

    @property
    def inner(self,inner):
        self.__inner = inner

    @inner.getter
    def inner(self):
        return self.__inner

    @inner.deleter
    def inner(self):
        del self.__inner

a = Prop3
a.inner = 22
print(a.inner)
print(a.__dict__)
del a.inner
print(a.__dict__)