def func1():
    yield 1
    yield func2
    yield 3

def func2():
    yield 3
    yield 4

if __name__ == '__main__':
    f1 = func1()
    for item in f1:
        print(item)