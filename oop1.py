# Повторение
class Plan:
    color = "red"
    parm = 12

    def myfunc(self,a):
        self.a = a
    def myinner():
        print('I am myinner')
       
obj = Plan()
obj.myfunc(2)
print(obj.a)
Plan.myinner()
#obj.myinner()
#############

obj.color = "green"
print(obj.color)
print(Plan.color)

        
