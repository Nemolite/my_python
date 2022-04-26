class Prop:
    def __init__(self,inner):
        self.__inner = inner

    def set_inner(self,inner):
        self.__inner = inner

    def get_inner(self):
        return self.__inner

    inner = property(set_inner,get_inner)

a = Prop
a.inner = 22
print(a.inner)