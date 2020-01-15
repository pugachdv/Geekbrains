#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

template_enterprise = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input('Наименование ' + str(i+1) + '-го предприятия: ')
    revenue_q1 = int(input('Прибыль за 1-й квартал: '))
    revenue_q2 = int(input('Прибыль за 2-й квартал: '))
    prevenue_q3 = int(input('Прибыль за 3-й квартал: '))
    revenue_q4 = int(input('Прибыль за 4-й квартал: '))
    template_enterprise[name] = Enterprise(
        q1=revenue_q1,
        q2=revenue_q2,
        q3=revenue_q3,
        q4=revenue_q4
    )

total_revenue = ()

for name, revenue in template_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(revenue)}')
    total_revenue += revenue

avg_revenue_total = sum(total_revenue) / len(template_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_revenue_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, revenue in template_enterprise.items():
    if sum(revenue) > avg_revenue_total:
        print(f'{name} - {sum(revenue)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, revenue in template_enterprise.items():
    if sum(revenue) < avg_revenue_total:
        print(f'{name} - {sum(revenue)}')
