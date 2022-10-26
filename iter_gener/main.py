# x = range(1, 10)


class MyRange:
    def __init__(self, start, finish, step=1):
        self.start = start
        self.finish = finish
        self.step = step

    def __iter__(self):
        self.cursor = self.start - self.step
        return self

    def __next__(self):
        self.cursor += self.step
        if self.cursor == self.finish:
            raise StopIteration
        return self.cursor


# for item in MyRange(1, 10):
#     print(item)

for i in range(3):
        print(i)