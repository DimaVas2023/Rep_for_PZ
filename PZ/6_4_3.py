# Дан список размера N. Переставить в обратном порядке элементы списка,
# расположенные между его минимальным и максимальным элементами, включая
# минимальный и максимальный элементы.


sp = []
sp_reversed = []


def create_list(i):
    try:
        sp.append(int(input(f'Введите {i} й элемент списка: ')))
    except:
        print('Элемент списка должен быть целым чилом!')
        create_list(i)
        

for i in range(int(input('Введите размер списка: '))):
    create_list(i)

max_num = max(sp)
index_max_num = 0
min_num = min(sp)
index_min_num = 0

for i, j in enumerate(sp):

    if j == max_num:
        index_max_num = i
    if j == min_num:
        index_min_num = i

sp_reversed = sp[:index_min_num:]+sp[index_min_num:index_max_num:-1]+sp[index_max_num::]
print(sp_reversed)

