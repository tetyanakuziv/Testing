year=int(input("Введите год "))
def func(year):
   if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
       print("Высокосный")
   else:
       print("Не высокосный")
func(year)