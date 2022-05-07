import math
class Derivate:
    def __init__(self,func):
        self.__fn = func

    def __call__(self,x,dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

def df_sin(x):
    return  math.sin(x)

df_sin_s = Derivate(df_sin)
print(df_sin(math.pi/4))
print(df_sin_s(math.pi/4))

@Derivate
def df_sin_d(x):
    return math.sin(x)
print(df_sin_d(math.pi/4))