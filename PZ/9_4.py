# Дан словарь с четным количеством элементов. Найти суммы значений
# элементов первой и второй половин с использованием функции. Результаты вывести
# на экран.


numbers = {}
summ_one = 0
summ_two = 0


def create_dict(i):
    try:
        numbers[i]=int(input('Введите число: '))
    except:
        print('Значение должно быть целым чилом!')
        create_dict(i)


# numbers = {i:int(input('Введите число')) for i in range(int(input('Введите чётное число')))}
try:
    n = int(input('Введите количество значений (чётное количество): '))
    if n%2 == 0:
        for i in range(n):
            create_dict(i)
    else:
        print('Введено нечётное число')
    
    for i in numbers:
        if i < len(numbers)//2:
            summ_one+=numbers[i]
        else:
            summ_two+=numbers[i]
    print(f'Сумма первой половины значений равна {summ_one}')
    print(f'Сумма второй половины значений равна {summ_two}')
except:
    pass