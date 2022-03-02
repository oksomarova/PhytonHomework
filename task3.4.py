# Задание 4
# вариант 1
res = lambda x, y: 1 / x ** abs(y)
print(res(2, -3))

# вариант 2
def my_func(x, y):
    res = 1
    while y < 0:
        res *= 1 / x
        y = y + 1
    return res
print(my_func(2, -3))
