def numeral_count(x):
    hop = 0
    while x > 10:
        x //= 10
        hop += 1
    return hop

def change_number(x):
    firstNum = x // (10 ** numeral_count(x))
    lastNum = x % 10
    x //= 10
    x = x - (firstNum * 10 ** numeral_count(x))
    x = lastNum * 10 ** (numeral_count(x) + 1) + x
    x *= 10
    x += firstNum
    print('Число наоборот:', x)
    return x

first_number = int(input('Введите первое число: '))
if first_number < 100:
    print('error')
else:
    change_number(first_number)
    second_number = int(input('Введите второе число: '))
    if second_number < 1000:
        print('error')
    else:
        change_number(second_number)
        print('Сумма чисел =', change_number(second_number) + change_number(first_number))
