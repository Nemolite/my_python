class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, step=1,*args, **kwargs):
        self.counter+=step
        print(self.counter)
        return self.counter

c = Counter()
c2 = Counter()
print(c.__dict__)
c()
c()

c2(2)
c2(2)