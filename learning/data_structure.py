
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
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    listMethod()
    createList()
