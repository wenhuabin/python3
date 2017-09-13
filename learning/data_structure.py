
def listMethod():
    a = []
    a.append(3)
    a.append(4)
    a[len(a):] = [5] #这个语法有点诡异
    a.extend([8,0])
    a.insert(5,10)
    a.insert(3,10)
    a.remove(10) #remove 10 is 10 exsits, the first one
    print(a.index(5)) #(5,start,end)
    #a.pop(1)
    #a.clear()
    a.sort()
    a.reverse()
    b = a.copy() #shallow copy, points to the same memory
    b[3] = 333
    print(a)
    print(b)

def createList():
    a = list(map(lambda x: x**2, range(10)))
    b = [x**2 for x in range(10)]
    c = [(x, y) for x in range(10) for y in range(20) if x != y]
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    d = [[row[i] for row in matrix] for i in range(4)]
    del d[0] # remove item from a list
    print(a)
    print(b)
    print(c)
    print(d)

def createTuple():
    a = 1,2,3,
    b = 1,
    print(a)
    print(b)
    print(len(a))

def createSet():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    for i, v in enumerate(basket):
        print(i, v)

def createDict():
    a = {x: x**2 for x in (2, 4, 6)}
    for k, v in a.items():
        print(k,v)

def condition():
    print(2 in [1,3])
    print(2 not in [1,3])
    # wrone example, maybe class
    print({1:3, 2:4} is {1:3, 2:4})
    print({1:3, 2:4} is not {1:3, 2:4})
    print((1, 2, 3) < (1, 2, 4))
    print('ABC' < 'C' < 'Pascal' < 'Python')

if __name__ == '__main__':
    listMethod()
    #createList()
    createTuple()
    createSet()
    createDict()
    condition()



