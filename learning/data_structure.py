
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


if __name__ == '__main__':
    listMethod()
