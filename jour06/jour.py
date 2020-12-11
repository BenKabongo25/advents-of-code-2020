# jour 6

def getStr(string):
    return string if not string.endswith('\n') else string[:-(len('\n'))]

with open('input.txt', 'r') as file:
    input = list(map(getStr,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(getStr,file.readlines()))

def func1(datas):
    datas.append('')
    n = 0
    res = []
    for data in datas:
        if data == '':
            n += len(res)
            res = []
        else:
            for c in data:
                if c not in res:
                    res.append(c)
    return n

def func2(datas):
    datas.append('')
    n = 0
    init = True
    res = []
    for data in datas:
        if data == '':
            n += len(res)
            res = []
            init = True
        else:
            if init and res == []:
                for c in data:
                    res.append(c)
            else:
                res2 = list(res)
                for r in res:
                    if r not in data:
                        res2.remove(r)
                res = list(res2)
            init = False
    return n

def test():
    print(func1(test1))
    print(func2(test1))
test()

print('Solutions')
print(func1(input))
print(func2(input))
