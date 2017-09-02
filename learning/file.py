def readFile():
    try:
        f = open('/Users/wenhuabin/Projects/p3/python3/files/test.txt', 'r')
        print(f.read())
    finally:
        if f:
            f.close()


#do not need to close
def readFileByWith():
    with open('/Users/wenhuabin/Projects/p3/python3/files/test.txt', 'r') as f:
        print(f.read())


def readByteFileByWith():
    with open('/Users/wenhuabin/Projects/p3/python3/files/github.png',
            'rb') as f:
        print(f.read())

def writeFileByWith():
    with open('/Users/wenhuabin/Projects/p3/python3/files/wtest.txt', 'w') as f:
        print(f.write("hello world teddy"))

readFile()
readFileByWith()
readByteFileByWith()
writeFileByWith()



