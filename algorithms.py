# name = input("What's your name? ")
# weight = int(input("How much do you weight? "))
# height = float(input("How tall are you? "))

# imc = weight/(height * height)
# if imc > 25:
#     print(name + " is overweight")
# else:
#     print(name + " is not overweight")

# number1 = int(input("Number 1: "))
# number2 = int(input("Number 2: "))
# number3 = int(input("Number 3: "))

# if number1 > number2 & number1 > number3:
#     print("Number 1 is the biggest number")
# elif number1 < number2 & number2 > number3:
#     print("Number 2 is the biggest number")
# else:
#     print("Number 3 is the biggest number")


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