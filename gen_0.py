
def hello_world(n):
    for i in range(n):
        yield 'hello world'


if __name__ == '__main__':
    for item in hello_world(4):
        print(item)
