# Задание предполагает, что у студента есть проект с практическими работами (NoNo 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS


import os


def size(pathf):
    for i in os.listdir(pathf):
        if os.path.isfile(i):
            os.path.getsize(i)


pz_11 = os.listdir('PZ_11')
print(pz_11)

os.makedirs('../test/test1')

os.replace('6_4_1.py', '/home/student/Документы/PycharmProject/IS-27/Proj 1sem Vasilchenko/Rep_for_PZ/test/6_4_1.py')
os.replace('6_4_2.py', '/home/student/Документы/PycharmProject/IS-27/Proj 1sem Vasilchenko/Rep_for_PZ/test/6_4_2.py')
os.replace('7_4_1.py', '/home/student/Документы/PycharmProject/IS-27/Proj 1sem Vasilchenko/Rep_for_PZ/test/test1/7_4_1.py')
os.rename('/home/student/Документы/PycharmProject/IS-27/Proj 1sem Vasilchenko/Rep_for_PZ/test/test1/7_4_1.py', '/home/student/Документы/PycharmProject/IS-27/Proj 1sem Vasilchenko/Rep_for_PZ/test/test1/test.txt')

for i in os.listdir():
    if os.path.isfile(i):
        os.path.getsize(i)

size('../test')
size('../test/test1')

short_file = '11111111111111111111111111'
for i in pz_11:
    if len(i) < len(short_file):
        short_file = i
print(short_file)

os.remove('/home/student/Документы/PycharmProject/IS-27/Proj 1sem Vasilchenko/Rep_for_PZ/test/test1/test.txt')

