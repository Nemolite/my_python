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


i = Iterator(1,7,1)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(next(i))


