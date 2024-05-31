# Diseñar una función que calcule el triple de un número y otra función que calcule el siguiente de un número.
# Utilizar las funciones en un programa para que ingresado un numero muestre el consecutivo del triple del número y el triple del consecutivo del número.
def triple(num):
   num3=3*num
   return num3
 
def consecutivo(num):
   consec = num + 1
   return consec
 
numero = int(input("Ingrese un numero"))
resultado = triple(numero)
resultado = consecutivo(resultado)
print("El consecutivo del triple del numero ingresado es: ", resultado)
resultado = consecutivo(numero)
resultado = triple(resultado)
print("El triple del consecutivo del numero ingresado es: ", resultado)