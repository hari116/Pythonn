# iterator

class NatNumIterator:

    def __iter__(self):
        self.a = 0
        return self

    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    def __next__(self):
        self.a += 1
        return self.a


class IterFibanocci:
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        x, y = self.a, self.b
        nxt = self.a + self.b
        self.a = self.b
        self.b = nxt
        return x, y


if __name__ == '__main__':
    inst = IterFibanocci()
    myiter = iter(inst)
    # print(next(myiter))
    for i in range(10):
        print(next(myiter)[1])
