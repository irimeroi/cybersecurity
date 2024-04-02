# 1) Calcular el sueldo de una persona conociendo la cantidad de horas que trabaja en el mes y el valor de la hora.
horasSemana = 40
valorHora = 20
sueldo = (horasSemana * 4) * valorHora
print(sueldo)

# 2) Solicitar dos datos: país y capital. Y luego muestre la capital del país. Ej. “Katmandú es la capital de Nepal”.
pais = input("Agregá un pais: ")
capital = input("Agregá su capital: ")
print(capital + " es la capital de " + pais)

# 3) Calcular el importe que debe pagar una persona por la compra de una heladera de pesos X y por pagar en efectivo le hacen el 10% de descuento. ¿Cuánto abona?
precioHeladera = int(input("Inserte el precio de la heladera: ").lower().strip())
efectivo = input("Paga en efectivo? ")

if efectivo == "si" or efectivo == "Si":
    descuento = precioHeladera*10/100
    precioEfectivo = precioHeladera-descuento
    print(precioEfectivo)
else:
    print(precioHeladera)

# 4) Hallar la longitud de la hipotenusa de un triángulo dada la medida de sus catetos. Hipotenusa2 = cateto2 c+cateto2
import math
cateto1 = int(input("Medida cateto 1 en cm: "))
cateto2 = int(input("Medida cateto 2 en cm: "))
print (math.sqrt((cateto1*cateto1) + (cateto2*cateto2)))

# 5) Ingresar un número de tres cifras y mostrar el segundo dígito. Ejemplo: se ingresa 358 y se debe mostrar 5
numero = input("Ingrese un número de tres cifras: ")
print(numero[1])

# 6) Ingresar un valor en millas y convertirlo a kilómetros y un valor en pulgadas y convertirlo a centímetros.
# 1 milla = 1.60935 km 1 pulgada = 2.534 cm
milla = 1.60935
addMilla = int(input("Ingrese un valor en millas: "))
millaEnKm = (addMilla*milla)
print(str(addMilla) + " millas convertidas a km son: " + str(millaEnKm) + "km")

pulgada = 2.534
addPulgada = int(input("Ingrese un valor en pulgadas: "))
pulgadaEnCm = (addPulgada*pulgada)
print(str(addPulgada) + " pulgadas convertidas a cm son: " + str(pulgadaEnCm) + " cm")

# 8) Ingresar un número. Si es positivo, calcular su raíz cuadrada, si es negativo mostrarsu cuadrado y si es cero mostrar “Error. Ha ingresado un valor nulo”
import math
numero = int(input("Ingrese un número: "))
if numero >= 0:
    print(math.sqrt(numero))
else:
    print("Error. Ha ingresado un valor nulo")

# 9) Ingresar las edades de dos personas. Si una de ellas es mayor de edad y la otra menor de edad, calcular y mostrar su promedio. En caso contrario mostrar las dos edades.
edad1 = int(input("Ingrese la edad de persona 1: "))
edad2 = int(input("Ingrese la edad de persona 2: "))

if edad1 >= 18 and edad2 <= 18 or edad1 <= 18 and edad2 >= 18:
    print("El promedio de las edades es: " + str((edad1+edad2)/2))
else:
    print("Las edades ingresadas son: " + str(edad1) + " y " + str(edad2))

# 11) Ingresar el valor de la ganancia anual de una empresa y calcular su retención segúnse encuentre dentro de los siguientes parámetros:
# <=10000 = cero, >10000 y <= 15000 = 2% sobre (ganancia -10000), and > 150000 = 300+5% sobre (ganancia -15000)
gananciaEmpresa = int(input("Ingrese la ganancia anual de su empresa: "))

if gananciaEmpresa > 10000 and gananciaEmpresa <= 15000:
    retencion = (gananciaEmpresa-10000)*2/100
    print("La retención es de: " + str(retencion))
elif gananciaEmpresa > 15000:
    retencion = ((gananciaEmpresa-15000)*5/100)+300
    print("La retención es de: " + str(retencion))
else:
    print("No hay retención")
    
# 13) Se ingresa el código de tipo de llamada: 1. Local 2. Interurbana 3. Internacional y la duración en minutos de la llamada.
# Si el minuto cuesta $3,25 para la llamada local,$2,40 para la llamada interurbana y $5,05 para la llamada internacional, diseñar unalgoritmo que permita calcular el monto a pagar por dicha llamada.
minutos = int(input("Ingrese la duración de la llamada en minutos: "))
codigo = int(input("Ingrese el codigo: "))
if minutos >= 0:
    if codigo == 1:
        print("El precio de la llamada es: " + str(minutos*3.25))
    elif codigo == 2:
        print("El precio de la llamada es: " + str(minutos*2.40))
    elif codigo == 3:
        print("El precio de la llamada es: " + str(minutos*5.05))
    else:
        print("El código ingresado es inválido")
else:
    print("La cantidad de minutos ingresados es inválida")

# 7) Ingresar dos números enteros y mostrar los valores intercambiados. Por ejemplo, si en a= 4 y b=10, se mostrará a=10 y b=4
    
# 10) Ingresar dos números, calcular la división entre el primero y el segundo, siempreque el segundo número no sea cero. En este último caso mostrar la leyenda “no sepuede realizar la división”.

# 12) Calcular el importe que debe pagar un auto en un estacionamiento teniendo encuenta como datos las horas y minutos de uso.
# El valor de la hora es de $700 y si los minutos exceden de 15, se incrementa una hora al importe. El mínimo para cobrares de una hora.
