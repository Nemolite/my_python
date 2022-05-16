class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p1 = Point(1,2)
p2 = Point(1,2)

print(hash(p1))
print(hash(p2))