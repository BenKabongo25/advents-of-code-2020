# jour 3

def getStr(string):
    return string if not string.endswith('\n') else string[:-(len('\n'))]

with open('input.txt', 'r') as file:
    input = list(map(getStr,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(getStr,file.readlines()))

def getChar(string, indice):
    return string[indice%len(string)]

def func1(datas, dx=3, dy=1):
    x, y = 0, 0
    nbArbre = 0
    while y < len(datas)-1:
        x += dx; y += dy
        if getChar(datas[y], x) == '#':
            nbArbre += 1
    return nbArbre

def func2(datas):
    return (func1(datas,1,1)*
            func1(datas,3,1)*
            func1(datas,5,1)*
            func1(datas,7,1)*
            func1(datas,1,2))

def test():
    print(func1(test1))
    print(func2(test1))
test()

print('Solutions')
print(func1(input))
print(func2(input))
