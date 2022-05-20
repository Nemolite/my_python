class Student:
    def __init__(self,name,ocen):
        self.name = name
        self.ocen = list(ocen)

    def __getitem__(self, item):
        return self.ocen[item]

    def __setitem__(self, key, value):
        self.ocen[key] = value

    def __delitem__(self, key):
        del self.ocen[key]

s1 = Student("Sergey",[2,3,4,5,6,7])
print(s1)
print(hash(s1))
print(s1.__dict__)
print(s1.ocen[2])

print(s1[2])

s1[3] = 34
print(s1.__dict__)

del s1[5]
print(s1.__dict__)