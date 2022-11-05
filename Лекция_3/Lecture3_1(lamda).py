# примеры функций lambda
# def sum(x):
#     return x + 10
sum = lambda x: x + 10

# def mult(x):
#     return x**2
mult = lambda x: x**2

# def sum1(x):
#     return x + 22
sum1 = lambda x: x + 22

# def mult1(x):
#     return x**3
mult1 = lambda x: x**3

# def sum2(x):
#     return x + 242
sum2 = lambda x: x + 242

# def mult2(x):
#     return x**5
mult2 = lambda x: x**5

print(mult(sum1(1)))

print(sum1(1))

print(mult(2))

def math(op, x):
    print(op(x))

math(sum1, 10)

math(sum2, 100)

# def sum4(x, y):
#     return x + y
sum4 = lambda x, y: x + y

def milt(x, y):
    return x * y

def calc(op, a, b):
    return print(op(a, b))
def calc1(op, a):
    return print(op(a))

calc1(sum, 4)

calc(sum4, 20, 30)

calc(lambda x, y: x + y, 20, 30)