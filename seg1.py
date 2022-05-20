class Student:
    def __init__(self,name,ocen):
        self.name = name
        self.ocen = list(ocen)

s1 = Student("Sergey",[2,3,4,5,6,7])
print(s1)
print(hash(s1))
print(s1.__dict__)
print(s1.ocen[2])

