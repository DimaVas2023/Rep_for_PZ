# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего регистра на нижний.

stop = [' ', '.', ',', '!', ':', '—']
count = 0
with open('text18-14.txt', 'r', encoding='utf-8',errors='ignore') as f:
    text = f.read()
    print(text)
    simbols = 0
    
    for i in text:
        if i.isalpha():
            simbols+=1
    print(f'Количество символов, принадлежащих к группе букв: {simbols}')

    for i in text:
        if i not in stop:
            count+=1
    with open('LowText18-14.txt', 'w', encoding='utf-8') as fn:
        for i in text:
            fn.write(i.lower())
print('Успешно завершено')