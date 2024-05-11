# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
# «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re


with open('hotline.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()
    three = len(re.findall('03', file_content))
    five = len(re.findall('50', file_content))
    print('номера телефонов горячих линий, связанных с ЕГЭ/ГИА:')
    for i in file_content.split('\n'):
        if 'ЕГЭ' in i or 'ГИА' in i:
            r = re.compile(r'\d+')
            t = r.search(i)
            print(t.group(0))
    print(f'\n{three} номеров телефонов заканчивается на «03»')
    print(f'{five} номеров телефонов заканчивается на «50»')

    with open('hotline2.txt', 'w', encoding='utf-8') as f:
        numerator = 0
        for i in file_content.split('\n'):
            if '«Горячая линия»' in i:
                f.write(i.replace('«Горячая линия»', '«Горячая линия Министерства образования Ростовской области»')+'\n')
                numerator+=1
            else:
                f.write(i+'\n')
        print(f'Количество добавлений - {numerator}')
    