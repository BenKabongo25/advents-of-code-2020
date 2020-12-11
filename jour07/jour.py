# jour 7

def getStr(string):
    return string if not string.endswith('\n') else string[:-(len('\n'))]

with open('input.txt', 'r') as file:
    input = list(map(getStr,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(getStr,file.readlines()))

with open('test2.txt', 'r') as file:
    test2 = list(map(getStr,file.readlines()))

def f(datas):
    res = {}
    for data in datas:
        containeur, contenu = data.split('contain')
        k = 'bag'
        if 'bags' in containeur: k = 'bags'
        containeur = containeur[:containeur.index(k)].strip()
        contenu = contenu.strip()
        res[containeur] = {}
        if 'no other' not in contenu:
            contenus = contenu.split(',')
            for i in range(len(contenus)):
                k = 'bag'
                if 'bags' in contenus[i]:
                    k = 'bags'
                contenus[i] = contenus[i][:contenus[i].index(k)].strip()
                nb = contenus[i].split(' ')[0]
                contenus[i] = contenus[i][len(nb)+1:]
                res[containeur][contenus[i]] = int(nb)
    return res

def func1(datas, value='shiny gold'):
    res = f(datas)
    def count(value=value, counted={}):
        n = 0
        for r in res:
            if value in res[r]:
                if r not in counted:
                    counted[r] = False
                    n += 1
        for c in list(counted):
            if not counted[c]:
                counted[c] = True
                n += count(c, counted)
        return n
    return count(value)

def func2(datas, value='shiny gold'):
    res = f(datas)
    def count(value):
        if res[value] == {}:
            return 0
        n = 0
        for v in res[value]:
            n += res[value][v] + res[value][v] * count(v)
        return n
    return count(value)

def test():
    print(func1(test1))
    print(func2(test1))
test()

print('Solutions')
print(func1(input))
print(func2(input))
