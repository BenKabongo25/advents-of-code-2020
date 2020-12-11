# jour 8

def getStr(string):
    return string if not string.endswith('\n') else string[:-(len('\n'))]

with open('input.txt', 'r') as file:
    input = list(map(getStr,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(getStr,file.readlines()))

def func1(datas):
    acc = 0
    i = 0
    ins = []
    while i not in ins:
        ins.append(i)
        data = datas[i]
        instruction, value = data.split(' ')
        instruction = instruction.strip()
        value = int(value)
        if instruction == 'acc':
            acc += value
            i += 1
        elif instruction == 'jmp':
            i += value
        elif instruction == 'nop':
            i += 1
    return acc

def func2(datas):
    def f(datas):
        acc = 0
        i = 0
        ins = []
        while True:
            if i in ins or i >= len(datas):
                return None
            ins.append(i)
            data = datas[i]
            instruction, value = data.split(' ')
            instruction = instruction.strip()
            value = int(value)
            if instruction == 'acc':
                acc += value
                i += 1
            elif instruction == 'jmp':
                i += value
            elif instruction == 'nop':
                i += 1
            if i == len(datas):
                return acc
    k = 0
    while True:
        d = list(datas)
        if 'jmp' in d[k]:
            d[k] = d[k].replace('jmp', 'nop')
            res = f(d)
            if res != None: return res
        elif 'nop' in d[k]:
            d[k] = d[k].replace('nop', 'jmp')
            res = f(d)
            if res != None: return res
        k += 1

def test():
    print(func1(test1))
    print(func2(test1))
test()

print('Solutions')
print(func1(input))
print(func2(input))
