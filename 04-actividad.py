#  Ingresar un número entero positivo A (validar el dato) y a continuación leer tantos números enteros como se ingresó en A. Se pide informar:
# El promedio de los números leídos.
# El porcentaje de los positivos impares.
# El valor máximo y mínimo leído.
primerNumero = int(input("Ingrese un número entero positivo: "))
totalNumeros = 0
positivos_impares = 0
porcentaje = 0
maximo = 0
minimo = float('inf')

if primerNumero <= 0:
    print("El número debe ser mayor a 0")

for num in range(primerNumero):
    numEnteros = int(input("Ingrese otros números enteros: "))
    totalNumeros = totalNumeros + numEnteros
    promedio = totalNumeros / primerNumero

    if numEnteros >= 0 and numEnteros % 2 != 0:
        positivos_impares += 1
        porcentaje = (positivos_impares/primerNumero)*100

    if numEnteros > maximo:
        maximo = numEnteros
    if numEnteros < minimo:
        minimo = numEnteros

# print(totalNumeros)
print(f"El promedio de todos los números es: {promedio}")
# print(f"Cantidad de positivos impares: {positivos_impares}")
print(f"El porcentaje de números positivos impares es: {porcentaje}%")
print(f"El valor máximo leído es: {maximo} y el valor mínimo: {minimo}")