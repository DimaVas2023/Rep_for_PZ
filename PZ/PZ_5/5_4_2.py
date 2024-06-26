# Описать функцию RectPS(x1,y1,х2,y2,P,S), вычисляющую периметр P и площадь S
# прямоугольника со сторонами, параллельными осям координат, по координатам (х1,
# y1), (х2, y2) его противоположных вершин (x1, y1, x2, y2 — входные, P и S —
# выходные параметры вещественного типа). С помощью этой функции найти
# периметры и площади трех прямоугольников с данными противоположными
# вершинами.

x1 = int(input('Введите x1 координату прямоугольника: '))
y1 = int(input('Введите y1 координату прямоугольника: '))
x2 = int(input('Введите x2 координату прямоугольника: '))
y2 = int(input('Введите y2 координату прямоугольника: '))

def RectPS(x1,y1,x2,y2=2):
    x = x2 - x1
    y = y2 - y1
    print('Площадь прямоугольника равна: ', abs(x*y))
    print('Периметр прямоугольника равен: ', abs(x*2+y*2))


try:
    RectPS(x1, y1, x2, y2)
except:
    print('введены не корректные данные')