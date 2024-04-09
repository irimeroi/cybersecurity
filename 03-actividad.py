# # # 1) Ingresar un numero entero mayor o igual a cero y continuación leer tantos números enteros como se ingresó en primer numero.
# # # se pide informar:
# # # El promedio de los numeros leídos pares (no incluye el primer numero).
# # # El porcentaje de los positivos impares múltiplos de 3.
# # # El valor máximo leído.
primer_numero = int(input("Ingresar un número mayor o igual a 0: "))
suma_numeros_pares = 0
total_numeros_pares = 0
promedio_numeros_pares = 0
total_positivos_impares = 0
porcentaje_positivos_impares = 0
valor_maximo = 0

for numero in range(primer_numero):
    numeros_agregados = int(input("Ingresar otros números: "))

    # promedio de los números pares ingresados
    if numeros_agregados > 0 and numeros_agregados % 2 == 0:
        suma_numeros_pares = suma_numeros_pares + numeros_agregados
        total_numeros_pares = total_numeros_pares + 1
        promedio_numeros_pares = suma_numeros_pares / total_numeros_pares

    # porcentaje de los números positivos impares múltiplos de 3
    if numeros_agregados > 0 and numeros_agregados % 3 == 0 and numeros_agregados % 2 != 0:
        total_positivos_impares = total_positivos_impares + 1
        porcentaje_positivos_impares = (total_positivos_impares/primer_numero)*100
        
    # valor máximo ingresado
    if numeros_agregados > valor_maximo:
        valor_maximo = numeros_agregados

print(f"La suma de números pares es: {suma_numeros_pares}")
print(f"El total de números pares es: {total_numeros_pares}")
print(f"El promedio de números pares excluyendo el primer número es: {promedio_numeros_pares}")
print(f"El total de positivos impares es: {total_positivos_impares}")
print(f"El porcentaje de positivos impares es: {porcentaje_positivos_impares}%")
print(f"El valor máximo leído es: {valor_maximo}")


# 2) Leer números enteros hasta que el numero leído sea múltiplo de 6. Se pide informar:
# Cantidad de datos leído.
# El valor mínimo y cuantas veces se repite.

numero = int(input("Ingresar un número: "))
total_numeros = 1
valor_minimo = 0
contador_valor_minimo = 0

while numero % 6 != 0:
    numero = int(input("Ingresar un número: "))
    total_numeros += 1

    if numero < valor_minimo:
        # si el valor mínimo es más grande que el número ingresado
        # 10 > 8
        # numero ingresado pasa a ser valor mínimo y se debería actualizar el contador
        numero = valor_minimo
        # contador_valor_minimo = 1
    # elif numero == valor_minimo:
        # si el valor minimo es igual al número ingresado
        # 8 = 8
        # aumentar el contador ya que hay que ver cuántas veces se repite
        # contador_valor_minimo +=1

    # else valor_minimo < numero:
        # 8 < 15
        # el valor minimo sigue siendo el mismo

print(f"El total de números ingresados es: {total_numeros}")
print(valor_minimo)

