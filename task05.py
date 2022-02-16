# Задание 5
revenue = float(input('укажите выручку в руб:'))
cost = float(input('укажите затраты в руб:'))
profit = revenue - cost
if profit > 0:
    headcount = int(input('укажите количество сотрудников:'))
    print('Прибыль составила:', profit, 'руб')
    margin = profit / revenue * 100             # не знаю, как % вывести и можно ли по условию округлить
    print('Рентабельность:', margin, '%;', 'Прибыль на одного сотрудника:', profit/headcount, 'руб')
else:
    print('Убыток составил:', profit, 'руб')