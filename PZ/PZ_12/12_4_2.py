# Составить генератор (yield), который выводит из строки только буквы.


def get_even(list_of_symbols) :
    for i in list_of_symbols:
        if i.isalpha():
            yield i
 
list_of_symbols = input('Введите текст: ')

for i in get_even(list_of_symbols):
    print (i, end = " ")

