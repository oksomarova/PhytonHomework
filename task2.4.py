# Урок 2. Задание 4

stroka = input('введите слова через пробел:').split()
for c, val in enumerate(stroka,1):
    print(c,val[:10])