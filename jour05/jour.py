# jour 5

def getStr(string):
    return string if not string.endswith('\n') else string[:-(len('\n'))]

with open('input.txt', 'r') as file:
    input = list(map(getStr,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(getStr,file.readlines()))

with open('test2.txt', 'r') as file:
    test2 = list(map(getStr,file.readlines()))

import math

def f(datas):
    res = []
    for data in datas:
        x0, y0 = 0, 0
        x1, y1 = 7, 127
        for c in data:
            if c == 'F':
                y1 = math.floor((y0+y1)/2)
            elif c == 'B':
                y0 = math.ceil((y0+y1)/2)
            elif c == 'R':
                x0 = math.ceil((x0+x1)/2)
            elif c == 'L':
                x1 = math.floor((x0+x1)/2)
        res.append(y0 * 8 + x0)
    return res

def func1(datas):
    return max(f(datas))

def func2(datas):
    res = f(datas)
    for i in range(min(res), max(res)+1):
        if i not in res:
            return i

def test():
    print(func1(test1))
    print(func1(test2))
    print(func2(test2))
test()

print('Solutions')
print(func1(input))
print(func2(input))
