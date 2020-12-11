# jour 10

with open('input.txt', 'r') as file:
    input = list(map(int,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(int,file.readlines()))

with open('test2.txt', 'r')   as file:
   test2 = list(map(int,file.readlines()))

import itertools
from collections import Counter

def func1(datas):
    datas2 = [0] + sorted(datas) + [max(datas)+3]
    def f(cur=0, datas=[], one=0, two=0, three=0):
        res = []
        for d in datas:
            if d - cur == 1: res.append(d)
            elif d - cur == 2: res.append(d)
            elif d - cur == 3: res.append(d)
        if res:
            mi = min(res)
            if mi - cur == 1: one += 1
            elif mi -cur == 2: two += 1
            elif mi - cur == 3: three += 1
        for v in datas2:
            if v <= cur: datas2.remove(v)
        if datas2 == []: return one * three
        return f(min(datas2), datas2, one, two, three)
    return f(0, datas2)

def func2(datas):
    datas.sort()
    datas.reverse()
    def pairwise(it):
        a, b = itertools.tee(it); next(b, None)
        return zip(a, b)
    d = []
    for i, j in pairwise(datas):
        if i - j == 1:
            d.append(1)
        elif i - j == 3:
            d.append(3)
    d.append(1)
    a = 0
    c = 0
    cTab = []
    for i in d:
        c += 1
        if a != i:
            c -= 1
            if a != 0 and i != 1:
                if c != 1:
                    cTab.append(str(c))
            c = 1
        a = i
    cTab.append(str(c))
    di = dict(Counter(cTab))
    res = 1
    for k, v in di.items():
        k = int(k); v = int(v)
        if k == 4:
            n = 7
        elif k == 3:
            n = 4
        elif k == 2:
            n = 2
        else:
            n = 1
        res = (n ** v) * res
    return res

def test():
    print(func1(test1))
    print(func1(test2))
    print(func2(test1))
    print(func2(test2))
test()

print('Solutions')
print(func1(input))
print(func2(input))
