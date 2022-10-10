original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10

print(inverted)

list = [1, 2, 3, 4, 5]
for i in list:
    print(i ** 2)

r = range(10)
for i in r:
    print(i)
