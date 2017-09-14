
def output():
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
        print(repr(x*x*x).rjust(4)[:2]) #truncation
    
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print('{0:10} ==> {1:10d}'.format(name, phone))

    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
        'Dcab: {0[Dcab]:d}'.format(table))


if __name__ == '__main__':
    output()
