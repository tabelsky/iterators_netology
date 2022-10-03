

class HelloWorld:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= self.n:
            raise StopIteration
        self.cursor += 1
        return 'hello world'


if __name__ == '__main__':
    for item in HelloWorld(4):
        print(item)
