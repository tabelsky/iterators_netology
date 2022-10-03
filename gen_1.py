

def my_range(start, finish):

    while start < finish:
        yield start
        start += 1


if __name__ == '__main__':
    for item in my_range(1, 5):
        print(item)
