# Дано вещественное число - цена 1кг конфет. Вывести стоимость 0.1, 0.2, и до 10 кг конфет

konfeta = int(input('Введите стоимость 1кг конфет: '))
for i in range(1, 11):
    print(f' стоимость {i/10} кг конфет - {konfeta * i / 10} рублей')
