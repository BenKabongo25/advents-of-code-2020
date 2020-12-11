# jour 9

with open('input.txt', 'r') as file:
    input = list(map(int,file.readlines()))

def f(datas, n=25):
    p = datas[:n]
    def get(x, p):
        res = []
        for a in p:
            if x-a != a and x-a in p:
                res.append((min(a, x-a), max(a, x-a)))
        return list(set(res))
    for i in range(n, len(datas)):
        x = datas[i]
        res = get(x, p)
        if not res:
            first = datas[i]
            if ((first-1 != 1 and first-1 in p) or
                (first+1 in p and x-first+1 in p)):
                p.append(x)
                res = [x]
            res = get(x, datas[:i])
        if not res: return x, i

def func1(datas, n=25):
    res = f(datas)
    return None if not res else res[0]

def func2(datas, n=25):
    res = f(datas,n)
    if res == None:
        return
    x, i = res
    for i in range(len(datas)):
        datas[i] = int(datas[i])
    def somme(datas):
        if len(datas) == 0:
            return []
        s = 0
        for i in range(len(datas)):
            s += datas[i]
            if s == x:
                return datas[:i+1]
        return somme(datas[1:])
    nombres = somme(datas[:i])
    return min(nombres)+max(nombres)

print('Solutions')
print(func1(input))
print(func2(input))
