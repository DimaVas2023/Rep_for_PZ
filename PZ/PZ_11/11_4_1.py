# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент:


import random


with open('Test-input.txt', 'w', encoding='utf-8') as f:
    for i in range(random.randint(5, 10)):
        f.write(f'{random.randint(-5, 5)}, ')


with open('Test-output.txt', 'w', encoding='utf-8') as fo:
    with open('Test-input.txt', 'r', encoding='utf-8') as fi:

        file = [int(i) for i in fi.read().split(', ')[:-1]]
        print(file)
        multilst = [i*max(file) for i in file]
        fo.write(f'Исходные данные: {file}\n')
        fo.write(f'Количество элементов: {len(file)}\n')
        fo.write(f'Минимальный элемент: {min(file)}\n')
        fo.write(f'Элементы умноженные на первый максимальный элемент: {multilst}\n')
print('Успешно завершено')