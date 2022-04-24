class Atrib:
    r = 10
    s2 = 20

    def __init__(self,r,s2):
        (self.r,self.s2) = (r,s2)

    def __getattribute__(self, item):
        print('Вы обратились к атрибуту',item)

    def __setattr__(self,key,value):
        print('Новое значение атрибута',key, value)

    def __getattr__(self, item):
        print("Вы обратились к не существующему атрибуту" + item)

t = Atrib(22,33)
t1 = t.r
t.s2 = 100
print(t.s3)
