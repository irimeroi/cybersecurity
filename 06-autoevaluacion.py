cont = 0
for i in range(1,10):
    a= int(input("ingrese un numero"))
    if (a%3==0):
        cont+=1
print(cont)

a=int(input("Ingrese un numero"))
b=int(input("Ingrese un numero"))
if a > 0 or a < b:
    c=a+b
if a < 0 and a < b:
    c=a-b
else:
    c= a*b
print (c) 

a=int(input("Ingrese un numero"))
b=int(input("Ingrese un numero"))
if a > 0 or a < b:
   c=a+b
   if a < 0 and a < b:
       c=a-b
else:
   c= a*b
print (c)

a=int(input("Ingrese un numero"))
b=int(input("Ingrese un numero"))
if a > 0 or a < b:
   c=a+b
   if a < 0 and a < b:
       c=a-b
   else:
       c= a*b
print (c)  

a=int(input("Ingrese un numero"))
b=int(input("Ingrese un numero"))
c=int(input("Ingrese un numero"))
if a>b or a>c and a<10:
   print(a+b+c)
if a!=0:
   print(a-b-c)

suma=0
for i in range(0,10):
  a=int(input("Ingrese un numero"))
suma=suma+a
p=suma/10
print(p)

suma=0
for i in range(0,10):
  a=int(input("Ingrese un numero"))
suma=suma+a
p=suma/10
print(p)

num=int(input("Ingrese la temperatura del dia"))
maxt=num
dia=1
for i in range (2, 31):
    num=int(input("Ingrese la temperatura del dia"))
    if num>maxt:
        maxt=num
        dia=i
print("El día de mayor temperatura fue el", dia)