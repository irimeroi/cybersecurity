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

# Diseñar un programa que permita ingresar las dimensiones de un ambiente
# rectangular y calcular utilizando funciones:
# a. La superficie del piso.
# b. La superficie de las paredes.
# c. El perímetro del ambiente.
# d. El costo de alfombrar el ambiente si el metro cuadrado de una alfombra cuesta $104.
# e. El costo pintar el ambiente sabiendo que un litro rinde 6 metros cuadrados y el litro cuesta $83.
def multiplicar(a, b):
   resultado = a * b
   return resultado

largo = int(input( 'Ingrese la medida del largo: '))
ancho = int(input( 'Ingrese la medida del ancho: '))
altura = int(input( 'Ingrese la medida de la altura: '))

superficie = multiplicar(largo, ancho)
print(f'La superficie de la habitacion es de {superficie} m2')

sup_paredes = multiplicar(multiplicar(largo, altura), 2) + multiplicar (multiplicar (ancho, altura), 2)
print(f'La superfifice de las paredes largas es de {sup_paredes}')

perimetro = multiplicar(largo + ancho, 2)
print(f'El perímetro es de {perimetro} metros')

alfombrar = multiplicar(superficie, 104)
print(f'El costo de alfombrar es de ${alfombrar}')

pintar = multiplicar((sup_paredes + superficie) / 6, 83)
print(f'El costo de pintar es de ${pintar:.2f}')