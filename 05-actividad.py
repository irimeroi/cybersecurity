#  Ingresar dos números y mostrar con el mensaje correspondiente:
# La suma.
# La diferencia.
# El producto.
# El resultado de elevar el primero al segundo.

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

print(numero1 + numero2)
if numero2 != 0:
    print(numero1 / numero2)
else:
    print("El segundo número debe ser distinto de 0 para poder realizar la división")
print(numero1 * numero2)
print(numero1 ** numero2)