# Дан список размера N. Найти номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

r = int(input('Введите размер списка: '))
sp = []
index = 0

def create_list(i):
    try:
        sp.append(int(input(f'Введите {i} й элемент списка: ')))
    except:
        print('Элемент списка должен быть целым чилом!')
        create_list(i)
        

for i in range(r):
    create_list(i)

max_num = max(sp)

for i, j in enumerate(sp):
    if j == max_num:
        index = i

print(f'Номер пооследнего локального макимума списка - {index}')