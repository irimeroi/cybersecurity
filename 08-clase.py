# "Insertar números enteros hasta que se ingrese un 0. Calcular max y min."
numeros = []
suma_arreglo = 0
n = int(input("Inserte números: "))

while n != 0:
    numeros.append(n)
    n = int(input("Inserte números: "))

for i in range(len(numeros)):
    print(numeros[i])

if len(numeros) > 0:
    for i in range(len(numeros)):
        suma_arreglo += numeros[i]
    promedio = suma_arreglo / len(numeros)
    print(f"El promedio es: {promedio}")
else:
    print("No se cargaron valores.")

for i in range(len(numeros)):
    if i == 0:
        maximo = numeros[i]
        pos_max = 0
        minimo = numeros[i]
        pos_min = 0
    if numeros[i] > maximo:
        maximo = numeros[i]
        pos_max = i
    if numeros[i] < minimo:
        minimo = numeros[i]
        pos_min = i
print(f"EL valor máximo del arreglo es {maximo} en posición {pos_max}")
print(f"El valor mínimo del arreglo es {minimo} en posición {pos_min}")
