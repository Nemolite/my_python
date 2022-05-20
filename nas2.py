class Basa:
    def __init__(self,x):
        self.x = x

class Nasled(Basa):
    def __init__(self,x,y):
        super().__init__(x)
        #Basa.__init__(self,x)
        self.y = y

n= Nasled(2,3)
print(n.__dict__)