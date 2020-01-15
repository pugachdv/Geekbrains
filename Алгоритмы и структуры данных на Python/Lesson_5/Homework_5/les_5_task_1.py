# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

k = int(input('Введите количество предприятий'))
New_Company = namedtuple('New_Company', 'name, first, second, third, fourth', defaults=[0, 0, 0, 0])

for i in range(1, k + 1):

    i = New_Company([input('Название'), float(input('1-ый квартал')), float(input('2-ой квартал')), float(input('3-ий квартал')), float(input('4-ый квартал'))])




#     enterprises[name].append(enterprises[name][1] / enterprises[name][0])
#
# print('Фактическая прибыль больше 10, но план не выполнен(<100%)')
#
# for key, value in enterprises.items():
#     if value[1] > 10 and value[2] < 1:
#         print(f'Предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')