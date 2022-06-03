kredit = float(input('Введите сумму кредита: '))
year = int(input('На сколько лет выдан? '))
persent = float(input('Под какой процент? '))

i = persent / 100
koeff = (i * (1 + i) ** year) / ((1 + i) ** year - 1)
payment = koeff * kredit

for period in range(1, 4):
    print('\nПериод:', period)
    print('Остаток долга на начало периода:', round(kredit, 2))
    print('Выплачено процентов:', round(kredit * i, 2))
    print('Выплачено основного долга:', round(payment - kredit * i, 2))
    kredit -= payment - kredit * i
print('\nОстаток долга:', kredit)

newYear = int(input('\nНа сколько лет продлевается кредит? '))
newPersent = float(input('Какой новый процент? '))

i = newPersent / 100
koeff = (i * (1 + i) ** (newYear + year - 3)) / ((1 + i) ** (newYear + year - 3) - 1)
payment = koeff * kredit

for newPeriod in range(4, (newYear + year + 1)):
    print('\nПериод:', newPeriod)
    print('Остаток долга на начало периода:', round(kredit, 2))
    print('Выплачено процентов:', round(kredit * i, 2))
    print('Выплачено основного долга:', round(payment - kredit * i, 2))
    kredit -= payment - kredit * i
print('\nКредит погашен!')