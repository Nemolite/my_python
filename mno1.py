# ножественное наследование
class Goods:
    def __init__(self,name,weight,price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name},{self.weight},{self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID +=1
        self.id = self.ID

    def seve_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")

class NoteBook(Goods,MixinLog):
    pass


n = NoteBook("Acer",1.5, 3000)
n.print_info()
n.seve_sell_log()
print(NoteBook.__mro__)
