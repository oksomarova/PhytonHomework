# Задание 5

def f():
    while True:
        li = list(map(int, input('введите целые числа через пробел, введите / для остановки:').split()))
        # почему не выводится текст для input?
        g = 0
        for el in li:
            if el != "/":
                g = g + el
                return g
            else:
            print('end of function')

total_sum = f()
print(total_sum)
