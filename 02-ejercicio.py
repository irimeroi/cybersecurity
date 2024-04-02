# 1) Realizar un algoritmo que le permita al usuario ingresar desde el teclado 2 números enteros
# Si los números ingresados no son mayores o iguales a cero informarlo y finalizar el programa, caso contrario, pedirle al usuario que ingrese uno de los siguientes operadores: + , - , * o /.
# El algoritmo deberá mostrar el resultado de la operación ingresada.

number1 = int(input("Ingresá un número: "))
number2 = int(input("Ingresá otro número: "))

if number1 >= 0 and number2 >= 0:
    operador = input("agregá uno de los siguientes +, -, * o /")
    if operador == "+":
        resultado = number1 + number2
        print(resultado)
    elif operador == "-":
        resultado = number1 - number2
        print(resultado)
    elif operador == "*":
        resultado = number1 * number2
        print(resultado)
    elif operador == "/":
        resultado = number1 / number2
        print(resultado)
    else:
        print("La operación no pudo ser realizada. Por favor intente nuevamente.")
else:
    print("Por favor ingrese números mayores o iguales a 0")