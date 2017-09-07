import itertools

#lambda: 匿名函数，有点类似于箭头函数

def icount():
    natuals = itertools.count(1)
    for i in natuals:
        print(i)

def icycle():
    cs = itertools.cycle('ABC')
    for c in cs:
        print(c)

def irepeat():
    cs = itertools.repeat('A', 3)
    for c in cs:
        print(c)

def itakew():
    na = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, na)
    print(list(ns))

def ichain():
    for c in itertools.chain('ABC', 'XYZ'):
        print(c)
        
def igroupby():
    for key, group in itertools.groupby('ABCBBBXYZAAA'):
        print(key, list(group))

def igroupbyf():
    for key, group in itertools.groupby('ABCBBbbXYZAAAaa', lambda c: c.upper()):
        print(key, list(group))

if __name__ == '__main__':
    #icycle()
    #irepeat()
    #itakew()
    #ichain()
    #igroupby()
    igroupbyf()
