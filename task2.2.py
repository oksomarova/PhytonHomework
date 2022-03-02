# Урок 2. Задание 2
li = input('введите элементы для списка через пробел и  нажмите enter:').split()
print(li)
n = len(li)
for i in range(1, n, 2):
    li[i-1], li[i] = li[i], li[i-1]
    print(li)










