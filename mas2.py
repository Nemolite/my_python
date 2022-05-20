class Iterator:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step =step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value +=self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self

ix = Iterator(1,7,1)
for x in ix:
    print(x)
