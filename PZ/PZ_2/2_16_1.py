# Дано трёхзначное число. Найти сумму и произведение его цифр
n = input('Введите трёхзначное число: ')
sum = 0
multiply = 1
try:
    if len(n) == 3:
        for i in n:
            sum += int(i)
            multiply *= int(i)
        print(f'Сумма цифр числа - {sum} \nПроизведение цифр числа - {multiply}')
    elif len(n) < 3 and int(n):
        print('Количество цифр меньше 3х ')
    elif len(n) > 3 and int(n):
        print('Количество цифр больше 3х')
except:
    print('Неверный ввод')