# задание 4
num = int(input('введите целое положительное число: '))
max = num % 10
num = num // 10
while num > 0:
    if num % 10 > max:
        max = num % 10
    num = num // 10
print("Значение найдено. Макс: ", max)