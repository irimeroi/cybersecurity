numeros_enteros = [40, 10, 20, 30]
max = 0
min = 100
cantidad_pares = 0
suma_pares = 0
print(numeros_enteros)

# Calcular el promedio de los elementos ubicados en las posiciones pares
for i in range(0, 4):
    if i % 2 == 0 or i == 0:
        suma_pares += numeros_enteros[i]
        cantidad_pares += 1
print(f"La suma de los pares es: {suma_pares}")
print(f"La cantidad de posiciones pares es: {cantidad_pares}")
print(f"EL promedio de los elementos ubicados en las posiciones pares es {suma_pares / cantidad_pares}")

# Calcular max y min
for i in range(len(numeros_enteros)):
    if numeros_enteros[i] > max:
        max = numeros_enteros[i]
    if numeros_enteros[i] < min:
        min = numeros_enteros[i]
print(f"El maximo es: {max}")
print(f"El minimo es: {min}")

mitad_max = max / 2
print(f"La mitad del numero maximo es: {mitad_max}")
pos_max = numeros_enteros.index(max)
numeros_enteros.insert(pos_max + 1, mitad_max)
print(numeros_enteros)

# Mostrar el arreglo ordenado de mayor a menor
numeros_enteros.sort(reverse=True)
print(f"Lista ordenada de mayor a menor: {numeros_enteros}")