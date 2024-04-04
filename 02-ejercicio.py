# 1) Realizar un algoritmo que le permita al usuario ingresar desde el teclado 2 números enteros
# Si los números ingresados no son mayores o iguales a cero informarlo y finalizar el programa, caso contrario, pedirle al usuario que ingrese uno de los siguientes operadores: + , - , * o /.
# El algoritmo deberá mostrar el resultado de la operación ingresada.

numero1 = int(input("Ingresá un número: "))
numero2 = int(input("Ingresá otro número: "))

if numero1 >= 0 and numero2 >= 0:
    operador = input("Agregá uno de los siguientes operadores: +, -, * o /")
    if operador == "+":
        resultado = numero1 + numero2
        print(resultado)
    elif operador == "-":
        resultado = numero1 - numero2
        print(resultado)
    elif operador == "*":
        resultado = numero1 * numero2
        print(resultado)
    elif operador == "/":
        resultado = numero1 / numero2
        print(resultado)
    else:
        print("La operación no pudo ser realizada. Por favor intente nuevamente.")
else:
    print("Los números ingresados deben ser mayores o iguales a 0")

