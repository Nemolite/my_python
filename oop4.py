# singleton
class Basa:
    __inst = None
    def __new__(cls,*args,**kwargs):
        if cls.__inst is None:
            cls.__inst = super().__new__(cls)      
        return cls.__inst
    def __init__(self,namedb,user,userpass):
        self.namedb = namedb
        self.user = user
        self.userpass = userpass
        

    def connetdb(self):
        print(f"Подключение к базе данных: {self.namedb}  {self.user}  {self.userpass}")

    def selectdb(self):
        print('Выборка из БД')

    def insert(self):
        print('Внесение в БД')

    def __del__(self):
        Basa.__inst = None

db = Basa('basa','user','pass')
print(db.__dict__)
print(db)
print(db.connetdb())
        
        
