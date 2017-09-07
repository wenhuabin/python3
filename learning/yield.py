from contextlib import contextmanager, closing
from urllib.request import urlopen

@contextmanager
def tag(name):
    print("<%s>:" % name)
    yield
    print("</%s>:" % name)

#@contextmanager
#def closing(thing):
#    try:
#        yield thing
#    finally:
#        thing.close()

if __name__ == '__main__':
    #with tag("h1"):
    #    print("hello")
    #    print("world!")

    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)


