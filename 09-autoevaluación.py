# def cambia(b):
#     b += 5
#     return
# a=3
# b=4
# cambia(a)
# cambia(b)
# print("a =", a, "b =", b)

# def calcula(a, b):
#     c = a**b
#     return
# n = int(input("Ingrese un número: "))
# while(n > 0):
#     calcula(n, 2)
#     print("La potencia es", c)
#     n = int(input("Ingrese un número: "))

import random

def calcular(a):
    cont = 0
    for i in range(1, a):
        if (a%i == 0):
            cont += 1

contg = 0
for i in range(1, 5):
    b = random.randint(2, 15)
    c = calcular(b)
    if (c==1):
        contg += 1
print(contg)

