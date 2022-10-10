numbers = [1, 2, 3, 4, 5]

ran = range(1, 6)
print(type(ran))

numbers = list(ran)
print(type(numbers))

print(numbers)
numbers[0] = 10
print(numbers)
numbers1 = []

for i in numbers:
    i *= 2
    numbers1.append(i)
    print(i)


print(numbers) # [10, 2, 3, 4, 5]
print(len(numbers))
print(numbers1)

colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)

colors.append('gray') # добавить в конец ['red', 'green', 'blue', 'gray']
print(colors)
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удаление элемента
