import pickle

def dumpAndSave():

    d = dict(name="huabin", age=20, score=99)
    with open('/Users/wenhuabin/Projects/p3/python3/files/test.txt', 'wb') as f:
        pickle.dump(d, f)

def readDumpFile():
    with open('/Users/wenhuabin/Projects/p3/python3/files/test.txt', 'rb') as f:
        d = pickle.load(f)
        print(d)

dumpAndSave()
readDumpFile()
