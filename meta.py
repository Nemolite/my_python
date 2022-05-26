def test(self):
    print("test")
    return True
A = type('Point',(), {'MAX_COORD':100,'MIN_COORD':0,'test':test})
pt = A()
print(pt.MAX_COORD)
print(pt.test())


