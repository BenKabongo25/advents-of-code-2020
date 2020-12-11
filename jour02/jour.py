# jour 2

with open('input.txt', 'r') as file:
    input = file.readlines()

with open('test1.txt', 'r') as file:
    test1 = file.readlines()

def func1(datas):
    n = 0
    for data in datas:
        code, password = data.split(':')
        code = code.strip(); password = password.strip()
        interval, letter = code.split(' ')
        interval = interval.strip(); letter = letter.strip()
        min, max = interval.split('-')
        min = int(min); max = int(max)
        if min <= list(password).count(letter) <= max:
            n += 1
    return n

def func2(datas):
    n = 0
    for data in datas:
        code, password = data.split(':')
        code = code.strip(); password = password.strip()
        pos, letter = code.split(' ')
        pos = pos.strip(); letter = letter.strip()
        pos1, pos2 = pos.split('-')
        pos1 = int(pos1); pos2 = int(pos2)
        if (password[pos1-1] == letter) ^ (password[pos2-1] == letter):
            n += 1
    return n

def test():
    print(func1(test1))
    print(func2(test1))
test()

print('Solutions')
print(func1(input))
print(func2(input))
