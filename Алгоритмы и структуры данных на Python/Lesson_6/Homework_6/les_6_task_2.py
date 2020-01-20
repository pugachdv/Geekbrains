from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input('Введите количество компаний: '))
total_profit = 0

for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название компании {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

average_profit = total_profit / num

print(f'\nСредняя прибыль = {average_profit}')

print(f'\nПредприятия с прибылью выше средней: ')
for comp in all_companies:
    if comp.profit > average_profit:
        print(f'Компания {comp.name} заработала {comp.profit}')

print(f'\nПредприятия с прибылью ниже средней: ')
for comp in all_companies:
    if comp.profit < average_profit:
        print(f'Компания {comp.name} заработала {comp.profit}')