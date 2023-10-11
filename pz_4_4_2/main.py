# Дано вещественное число - цена 1кг конфет. Вывести стоимость 0.1, 0.2, и до 10 кг конфет

# konfeta = int(input())
# for i in range(1, 11):
#     print(f' стоимость {i/10} кг конфет - {konfeta * i / 10} рублей')


n = int(input())
print(n%10)

n = int(input())
print(n%10,n//10)

n = int(input())
print(n%10,(n//10)%10,n//100)

n = int(input())
print(n%10,(n//10)%10,(n//100)%10, n//1000)
#
n = int(input())
print(n%10,(n//10)%10,(n//100)%10,(n//1000)%10,n//10000)

n = int(input())
print(n%10,(n//10)%10,(n//100)%10,(n//1000)%10,(n//10000)%10,n//100000)