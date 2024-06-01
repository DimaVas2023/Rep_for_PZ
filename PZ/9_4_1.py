# Дан словарь с четным количеством элементов. Найти суммы значений
# элементов первой и второй половин с использованием функции. Результаты вывести
# на экран.

import random

numbers = {i:random.randint(0, 4) for i in range(4)}
summ_one = 0
summ_two = 0



# numbers = {i:int(input('Введите число')) for i in range(int(input('Введите чётное число')))}

print(f'Данный словарь: {numbers}')

for i in numbers:
    if i < len(numbers)//2:
        summ_one+=numbers[i]
    else:
        summ_two+=numbers[i]
print(f'Сумма первой половины значений равна {summ_one}')
print(f'Сумма второй половины значений равна {summ_two}')

