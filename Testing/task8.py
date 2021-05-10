import random
a = int(input("Введите минимальное значение первого списка "))
b = int(input("Введите максимальное значение первого списка "))
n = int(input("Введите длину первого списка "))
c =int(input("Введите минимальное значение второго списка "))
d =int(input("Введите максимальное значение второго списка "))
s =int(input("Введите длину второго списка "))
firstList = [random.randint(a,b) for i in range(n)]
secList = [random.randint(c,d) for i in range(s)]
print(firstList, secList)
res = [x for x in firstList + secList if x not in firstList or x not in secList]
print(res)
if not res:
    print("Списки одинаковые")
else:
    print("Списки не одинаковые")
