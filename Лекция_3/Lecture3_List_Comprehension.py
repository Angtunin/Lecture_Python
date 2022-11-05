# Создать список из чётных чисел от 1 до 100

list = []

for i in range(1, 101):
    if i % 2 == 0:
        list.append(i)

print(list)

list1 = [i for i in range(1, 101) if i % 2 == 0]

print(list1)

list2 = [(i, i) for i in range(1, 101) if i % 2 == 0]

print(list2)

def f(x):
    return x**2

list3 = [(i, f(i)) for i in range(1, 101) if i % 2 == 0] # кортеж число и его вторая степень
print(list3)

list4 = [f(i) for i in range(1, 101) if i % 2 == 0] # вторая степень чётных чисел 
print(list4)