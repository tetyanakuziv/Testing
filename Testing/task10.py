a = list(map(int, input("Введите число больше 9 ")))
print (a)
def listsum(a):
    theSum = 0
    for i in a:
        theSum = theSum + i
    print (theSum)
listsum(a)