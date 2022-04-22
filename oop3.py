class Intyer:
    def __new__(cls,*args,**kwargs):
        print('new')
        #return super().__new__(cls)

    def __init__(self,x,y):
        self.x = x
        self.y = y

in1 = Intyer(3,4)
#print(in1.__dict__)
print(in1)
