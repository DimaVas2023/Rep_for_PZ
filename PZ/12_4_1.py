# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

import random

el = [random.randint(0, 5) for i in range(6)]
print(f'Список чисел для умножения: {el}')
try:
    multiply = int(input('Введите множитель: '))
    for i in range(len(el)):
        print(el[i]*multiply)
except:
    print('Введите целое число')

