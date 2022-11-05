"""
В файле хранятся числа, нужно выбрать четные и
составить список пар (число; квадрат числа).
Пример:
1 2 3 5 8 15 23 38
Получить:
[(2, 4), (8, 64), (38, 1444)]
"""
# path = '/1/Проекты/GeekBrains/Python/Лекции/Лекция_3/data_3_1.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
#
# numbers = []
#
# while data != '': # проверка пока строка не пустая
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# решение (запись) с помощью lamda

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x**2), res)
print(data)
print(res)