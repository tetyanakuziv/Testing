import random
a = int(input("Введите минимальное значение списка"))
b = int(input("Введите максимальное значение списка"))
n = int(input("Введите длину списка"))
list = [random.randint(a,b) for i in range (n)]
print(list)