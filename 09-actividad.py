# # En base a los conceptos vistos en el módulo, debés realizar el siguiente ejercicio: 
# # Dos números son amigos si cada uno de ellos es igual a la suma de los divisores del otro.

# # Por ejemplo, 220 y 284 son amigos ya que:
# # La suma de divisores de 284 es 1 + 2 + 4 + 71 + 142 = 220
# # La suma de divisores de 220 es:
# # 1 + 2 + 4 + 5 + 10 + 11 + 20 +22 + 44 + 55 + 110 = 284
# # Construir un algoritmo usando funciones y luego codificarlo en Python para que dados dos números determine si son amigos.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
divisores1 = []
divisores2 = []
suma1 = 0
suma2 = 0

for i in range(1, numero1):
    if numero1 % i == 0:
        suma1 += i
        divisores1.append(i)

for j in range(1, numero2):
    if numero2 % j == 0:
        suma2 += j
        divisores2.append(j)

if suma1 == numero2 and suma2 == numero1:
    print("Los numeros son amigos!")
else:
    print("Los numeros seleccionados no son amigos!")
print(f"Los divisores del primer numero son: {divisores1} y su suma iguala a {suma1}")
print(f"Los divisores del primer numero son: {divisores2} y su suma iguala a {suma2}")

# -----------------------------------------
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

if suma_divisores(numero1) == numero2 and suma_divisores(numero2) == numero1:
    print("Los números son amigos!")
else:
    print("Los numeros seleccionados no son amigos!")
