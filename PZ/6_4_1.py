#Дан первый член A и знаменатель D геометрической прогрессии. Сформировать и
# вывести список размера 10, содержащий 10 первых членов данной прогрессии: A,
# A* D, A* D**2, A*D**3, ... .

a = int(input('Введите первый член геометричесой прогрессии: '))
d = int(input('Введите знаменатель геометричесой прогрессии: '))
geom_p = []
for i in range(1, 11):
    geom_p.append(a*d**i)
print(f'10 первых членов геометрической прогрессии вида: A* D, A* D**2, A*D**3 \n{geom_p}')