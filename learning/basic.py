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


