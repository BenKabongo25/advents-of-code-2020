# jour 4

def getStr(string):
    return string if not string.endswith('\n') else string[:-(len('\n'))]

with open('input.txt', 'r') as file:
    input = list(map(getStr,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(getStr,file.readlines()))

with open('test2.txt', 'r') as file:
    test2 = list(map(getStr,file.readlines()))

KEYS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

def func1(datas, keys=KEYS[:-1]):
    datas.append('')
    n = 0
    keysCount = [0]*(len(keys))
    for data in datas:
        if data == '':
            if 0 not in keysCount:
                n += 1
            keysCount = [0]*(len(keys))
        else:
            keysValues = data.split(' ')
            for kv in keysValues:
                k, v = kv.split(':')
                k = k.strip(); v = v.strip()
                if k != KEYS[-1]:
                    keysCount[keys.index(k)] = 1
    return n

def func2(datas, keys=KEYS[:-1]):
    datas.append('')
    n = 0
    keysCount = [0]*(len(keys))
    for data in datas:
        if data == '':
            if 0 not in keysCount:
                n += 1
            keysCount = [0]*(len(keys))
        else:
            keysValues = data.split(' ')
            for kv in keysValues:
                k, v = kv.split(':')
                k = k.strip(); v = v.strip()
                if k == 'byr':
                    if 1920 <= int(v) <= 2002:
                        keysCount[keys.index(k)] = 1
                elif k == 'iyr':
                    if 2010 <= int(v) <= 2020:
                        keysCount[keys.index(k)] = 1
                elif k == 'eyr':
                    if 2020 <= int(v) <= 2030:
                        keysCount[keys.index(k)] = 1
                elif k == 'hgt':
                    if 'cm' in v:
                        v = v[:-2]
                        if 150 <= int(v) <= 193:
                            keysCount[keys.index(k)] = 1
                    elif 'in' in v:
                        v = v[:-2]
                        if 59 <= int(v) <= 76:
                            keysCount[keys.index(k)] = 1
                elif k == 'hcl':
                    if v[0] == '#':
                        check = True
                        for c in v[1:]:
                            if c.lower() not in 'abcdef1234567890':
                                 check = False
                        if check:
                            keysCount[keys.index(k)] = 1
                elif k == 'ecl':
                    if v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                        keysCount[keys.index(k)] = 1
                elif k == 'pid':
                    if len(v) == 9:
                        check = True
                        for c in v:
                            if c not in '1234567890':
                                check = False
                        if check:
                            keysCount[keys.index(k)] = 1
                else:
                    pass
    return n

def test():
    print(func1(test1))
    print(func1(test2))
    print(func2(test1))
    print(func2(test2))
test()

print('Solutions')
print(func1(input))
print(func2(input))
