# Jour 1

with open('input.txt', 'r') as file:
    input = list(map(int,file.readlines()))

with open('test1.txt', 'r') as file:
    test1 = list(map(int,file.readlines()))

def func1(datas):
    for i in range(len(datas)):
        for j in range(i+1, len(datas)):
            di = datas[i]
            dj = datas[j]
            if di + dj == 2020:
                return di * dj

def func2(datas):
    for i in range(len(datas)):
        for j in range(i+1, len(datas)):
            for l in range(j+1, len(datas)):
                di = datas[i]
                dj = datas[j]
                dl = datas[l]
                if di + dj + dl == 2020:
                    return di * dj * dl

def test():
    print("Tests")
    print(func1(test1))
    print(func2(test1))
test()

print("Solutions")
print(func1(input))
print(func2(input))
