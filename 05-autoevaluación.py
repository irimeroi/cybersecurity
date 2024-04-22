a = 3.5
b = 8
print(a+b*a)

# Esto falla porque la variable 'a' guarda una string, mientras que la variable 'b' guarda un interger, y Python no puede sumar diferentes tipos de datos.
a = input("ingrese un numero")
b=int(input("ingrese un numero"))
c=(a+b)/2
print(c)

a=int(input("ingrese un numero"))
b=int(input("ingrese un numero"))
c=(a+b)*(a-b)
d=a**2-b**2
print(c)
print(d)

a=101
b=a%10
c=a//10
d=c%10
e=c//10
f=e%10
print(b,d,f) # b = 1, d = 0, f = 1