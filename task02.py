#задание 2
t = int(input('введите количество секунд:'))
min = t // 60
sec = t % 60
hours = min // 60
min = min % 60
print(hours, ':', min, ':', sec)
