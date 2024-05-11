# Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
# источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
# книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
# Название книги, Год выпуска, Аннотация.

import sqlite3 as sq
import random


typ = ['видения', 'новелла', 'ода', 'поэма', 'повесть']
countr = ['Австралия', 'Белоруссия', 'Великобритания', 'Канада', 'Россия']
aut = ['Лев Толстой', 'Джордж Оруэлл', 'Джеймс Джойс', 'Уильям Фолкнер']
description = 'что бы завершить введите 0\nчто бы добавить запись введите 1\nчто бы удалить запись введите 2\nчто бы начать поиск введите 3\nчто бы обновить запись введите 4\nчто бы вывести данные из таблицы введите 5'
l = 11
separator = ', '


        
def drop():
    print('На ввод ожидается 2 значения через запятую:\nстолбец, значение')
    s, n = input(': ').split(separator)
    try:
        with sq.connect('LibraryDB.db') as con:
            cur = con.cursor()
            cur.execute(f"""DELETE FROM library WHERE '{s}' == '{n}';
                """)
            con.commit()
        print('✔')
    except:
        print('error')
        

def search():
    print('На ввод ожидается 2 значения через запятую:\nстолбец для поиска, значение')
    s, n = input(': ').split(separator)
    try:
        with sq.connect('LibraryDB.db') as con:
            cur = con.cursor()
            data = cur.execute(f"""SELECT * FROM library WHERE '{s}' == '{n}';
                """).fetchall()
            print(data)
        print('✔')
    except:
        print('error')
    
def update():
    print('На ввод ожидается 4 значения через запятую:\nстолбец для изменения, значение в нём, столбец для нового значения, новое значение')
    s, n, s1, n1 = input(': ').split(separator)
    try:
        with sq.connect('LibraryDB.db') as con:     
            con.cursor()
            cur.execute(f"""UPDATE library SET '{s1}' = '{n1}' WHERE '{s}' == '{n}';
                """)
            con.commit()
        print('✔')
    except:
        print('error')
        
    
def add():
    print('На ввод ожидается 4 значения через запятую:\nжанр книги, страна издания, серия, автор')
    t, c, s, a = input(': ').split(separator)
    try:
        with sq.connect('LibraryDB.db') as con:
            cur = con.cursor()
            cur.execute(f"""INSERT INTO library(type, country, series, autor) VALUES('{t}', '{c}', '{s}', '{a}');
                """)
            con.commit()
        print('✔')
    except:
        print('error')

def show():
    try:
        with sq.connect('LibraryDB.db') as con:
            cur = con.cursor()
            data = cur.execute(f"""SELECT * FROM library;
                """).fetchall()
            for i in data:
                print(i)
        print('✔')
    except:
        print('error')


with sq.connect('LibraryDB.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS library')
    cur.execute("""CREATE TABLE library(
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                type VARCHAR(50) NOT NULL,
                country VARCHAR(20) NOT NULL,
                series VARCHAR(30),
                autor VARCHAR(20) NOT NULL);
                """)

with sq.connect('LibraryDB.db') as con:
    cur = con.cursor()
    for i in range(10):
        cur.execute(f"""INSERT INTO library(type, country, series, autor) VALUES('{typ[random.randint(0, len(typ)-1)]}', '{countr[random.randint(0, len(countr)-1)]}', 
                                '{random.randint(1,65536)}', '{aut[random.randint(0, len(aut)-1)]}');""")        
    con.commit()

with sq.connect('LibraryDB.db') as con:
        cur = con.cursor()
        data = cur.execute(f"""SELECT * FROM library;
            """).fetchall()
        print(data)


print(description)
while True:
    try:
        l = input('Введите значение: ')
        if l == '0':
            print('Соединение закрыто')
            break
        elif int(l) > 5:
            print('Введён неправильный номер команды')
            break
        elif int(l) < 0:
            print('Введён неправильный номер команды')
            break

        if l == '1':
            add()
        if l == '2':
            drop()
        if l == '3':
            search()
        if l == '4':
            update()
        if l == '5':
            show()

    except:
        print('Введены неверные данные')