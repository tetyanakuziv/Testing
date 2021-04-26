a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
op = input("Виберіть операцію: + - * / ")
def func(a, b):
    if op == "+":
       print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        if b>0:
            print(a/b)
        elif b==0:
            print("Введіть число більше нуля")

func(a,b)