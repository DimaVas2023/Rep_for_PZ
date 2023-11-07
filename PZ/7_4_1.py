#Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных)
#букв латинского алфавита.


latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
try:
    n = int(input('Введите целое число от 1 до 26: '))
    if 1<n<26:
        print([latin[i] for i in range(n)])
    else:
        print('1 и 26 не включаются в диапозон')
except:
    print('Введите целое число')