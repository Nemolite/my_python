class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter+=1
        print(self.counter)
        return self.counter

c = Counter()
print(c.__dict__)
c()
c()

