import sys

def testWhileElse():
    count = 0
    while count < 5:
        print(count)
        count += 1
    else:
        print(count, 'false')

def testForElse():
    #else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况
    #下执行，while … else 也是一样
    for num in range(10,20):  # 迭代 10 到 20 之间的数字
    	for i in range(2,num): # 根据因子迭代
    	   if num%i == 0:      # 确定第一个因子
    	      j=num/i          # 计算第二个因子
    	      print('%d 等于 %d * %d' % (num,i,j))
    	      break            # 跳出当前循环
    	else:                  # 循环的 else 部分
    	   print(num, '是一个质数')

def forStep():
    arr = ['a','b','c']
    for i in range(0, 10, 3):
        print(i)
    for i, val in enumerate(arr):
        print(i, val)

def testIn(x):
    if x in ['1','2',3]:
        print('in')
    else:
        print('out')

def funcParams(x, y=1,n='hello'):
    print(x)
    print(y)
    print(n)

def funcMutable(a, L=[]):
    L.append(a)
    return L

#Python doesn't copy objects you pass during a function call ever.
#Function parameters are names. When you call a function Python binds
#these parameters to whatever objects you pass (via names in a caller scope).
#Objects can be mutable (like lists) or immutable (like integers, strings in
#Python). Mutable object you can change. You can't change a name,
#you just can bind it to another object.

def funcMutableNone(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

def passParamsTest(x):
    x=3

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def main():
    #sys argvs, sys.argv[0] being the program itself
    print('Hello there', sys.argv[1]) 



if __name__ == '__main__':
    testWhileElse()
    testForElse()
    #main()
    forStep()
    testIn(3)
    testIn('c')
    funcParams(3)
    funcParams(3, 2)
    funcParams(3, 3,'world')
    print(funcMutable(3))
    print(funcMutable(4))
    print(funcMutableNone(4))
    print(funcMutableNone(5))
    x = 4
    passParamsTest(x)
    print(x)
    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           test="Hello World!",
	   #'hello', SyntaxError: positional argument follows keyword argument
           sketch="Cheese Shop Sketch")


