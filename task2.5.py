#5. Урок 2. Задание 5
string = input('введите набор чисел через пробел:').split()
for i in range(len(string)):
    string[i] = int(string[i])
print(sorted(string, reverse = True))
string = sorted(string, reverse = True)
num = int(input('введите одно новое число:'))
i = 0
for el in string:
    if num <= el:
        i = i+1
string.insert(i, num)
print(string)


