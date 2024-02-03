# 1. В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.




rows_matrix = int(input('Введите количество строк матрицы: '))
matrix = [([i for i in range(1, rows_matrix+1)]) for i in range(rows_matrix)]
numerator = 0

print('\nИсходная матрица:')
for i in range(len(matrix)):
    print(matrix[i])
print('\nИзменённая:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # print(j, numerator)
        if j != numerator:
            matrix[i][j] = matrix[i][j]*2
    numerator+=1
    print(matrix[i])
    