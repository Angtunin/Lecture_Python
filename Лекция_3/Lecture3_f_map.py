li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x: x + 10, li))
print(li)

data = map(int, '1, 2, 3, 4, 5'.split(','))

for e in data:
    print(e)

print('--' * 100)

for e in data: # итератор map срабатывает один раз, поэтому нужно сохранять в список
    print(e)

data = list(map(int, '1, 2, 3, 4, 5'.split(',')))

for e in data:
    print(e)

print('--' * 100)

for e in data:
    print(e)

# обработка (преобразование) списка с помощью map

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res) )
print(data)
print(res)

data = list(map(int, input().split())) # ввод чисел с клавиатуры через пробел
print(data)