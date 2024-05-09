# 1) Se ingresan 100 números enteros positivos, por cada número ingresado se le solicita
# al operador que seleccione la operación a realizar: si el operador ingresa 1, el
# programa debe devolver el factorial del número ingresado; si el operador ingresa 2
# el programa debe solicitarle al operador la potencia a la cual quiere elevar el número
# ingresado y debe mostrar el resultado y; para cualquier otro valor de operación, el
# programa debe informar si el numero ingresado es par, impar o nulo

for numeros in range(1, 3, 1):
    numero = int(input("Ingrese números enteros positivos: "))
    while numero < 0:
        numero = int(input("El número debe ser mayor o igual a 0: "))

    user_choice = int(input(f"Ingrese una opción:\n1. Devuelve el factorial\n2. Calcula la potencia\n3. Determina si el número es par, impar, o nulo: "))

    if user_choice == 1:
        factorial = 1
        for i in range(numero, 0, -1):
            print(i)
            factorial *= i
        print("El factorial del número ingresado es: ", factorial)
    elif user_choice == 2:
        potencia = int(input("Ingrese la potencia a la cual quisiera elevar el número: "))
        resultado = numero ** potencia
        print(resultado)
    elif user_choice == 3:
        if numero == 0:
            print("El número es nulo.")
        elif numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    else:
        user_choice = int(input("Por favor ingrese un número del 1 al 3: "))

# ------------------------------------------------------------------------------
# Se ingresan el mes (validar entre 0 y 12), la cotizacion de dolár blue (validar que no sea negativo) y la cotizacion del dolar mep(Validar que no esa negativa) hasta que el mes sea cero.
# Calcular y mostrar:
# a) EL mes donde la diferencia entre el dolar blue y el dolar mep sea minima
# b) El promedio de la cotizacion del dolar blue en los meses pares.
# c) El mes donde se registro el maximo valor del dolar mep
# d) Mostrar la diferencia entre el dolar blue y el mep de cada mes ingresado
# e) Calcular el porcentaje de la diferencia del dolar blue con respecto al dolar mep
cont = 1
cont_blue = 0
acum = 0
minimo = 0
mes_minimo = 0
maximo = 0
mes_maximo = 0

mes = int(input("Ingrese el mes (0-12): "))
while mes < 0 or mes > 12:
    print("Error - Ingrese nuevamente el mes.")
    mes = int(input("Ingrese el mes (0-12): "))
    
while mes != 0:
    cont += 1
    blue = int(input("Ingrese cotización dolar blue: "))
    while blue <= 0:
        print("Error = ingrese nuevamente la cotización.")
        blue = int(input("Ingrese cotización dolar blue: "))
    mep = int(input("Ingrese cotización dolar mep: "))
    while mep <= 0:
        print("Error = ingrese nuevamente la cotización.")
        mep = int(input("Ingrese cotización dolar mep: "))
    
    if cont == 1:
        minimo = blue-mep
        maximo = blue
    if blue-mep <= minimo:
        minimo = blue-mep
        mes_minimo = mes
        mes_minimo = 1
        mes_maximo = 1
    if mes % 2 == 0:
        acum = acum - blue
        cont_blue += 1
    if blue <= maximo:
        maximo = blue
        mes_maximo = mes
    print(f"La diferencia entre el dólar blue y el dólar mep es: {blue - mep}")
    print(f"El porcentaje de la diferencia entre el dólar blue y el dólar mep es: {(blue-mep)*100/blue}")
    
    mes = int(input("Ingrese el mes (0-12): "))
    while mes < 0 or mes > 12:
        print("Error - Ingrese nuevamente el mes.")
        mes = int(input("Ingrese el mes (0-12): "))
print(f"El mínimo de la diferencia fue en el mes {mes_minimo}")
if cont_blue != 0:
    print(f"El promedio es {acum/cont_blue}")
else:
    print("No se puede calcular el promedio.")

# ------------------------------------------------------------------------------
# 2) Una empresa liquida sueldos según la categoría de cada empleado y paga por hora
# según la siguiente tabla:
# • categoría 1: $4500
# • categoría 2: $5000
# • categoría 3: $5500
# • categoría 4: $5800
# Diseñar un programa que permita ingresar la categoría de cada empleado y las horas
# que trabajó en el mes y calcule:
# a) Calcular el sueldo bruto y el sueldo neto (descontar 17% de aportes) de cada
# empleado.
# b) Calcular el total de sueldos que paga la empresa.
# c) Determinar cuántos empleados de cada categoría hay.
categoria1 = 0
categoria2 = 0
categoria3 = 0
categoria4 = 0
total_saldos = 0

categoria = int(input("Ingrese la categoría (1, 2, 3 o 4): "))
while categoria < 1 or categoria > 4:
    print("Error - intente nuevamente.")
    categoria = int(input("Ingrese la categoría (1, 2, 3 o 4): "))

while categoria != 0:
    if categoria < 1 or categoria > 4:
        print("Por favor ingrese un número del 1 al 4: ")
    else:
        if categoria == 1:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 4500
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
            categoria1 += 1
            total_saldos += sueldo_bruto

        elif categoria == 2:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 5000
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
            categoria1 += 2
            total_saldos += sueldo_bruto

        elif categoria == 3:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 5500
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
            categoria1 += 3
            total_saldos += sueldo_bruto

        elif categoria == 4:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 5800
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
            categoria1 += 4
            total_saldos += sueldo_bruto

        else:
            print("Ha habido un error, por favor intente nuevamente")    
    categoria = int(input("Ingrese la categoría (1, 2, 3 o 4): "))

print("La cantidad de empleados en la categoría 1 es: ", categoria1)
print("La cantidad de empleados en la categoría 2 es: ", categoria2)
print("La cantidad de empleados en la categoría 3 es: ", categoria3)
print("La cantidad de empleados en la categoría 4 es: ", categoria4)
print(f"El total de sueldos que paga la empresa es: {total_saldos}")

# ------------------------------------------------------------------------------
# En un reconocido banco de la Ciudad de Buenos Aires, los clientes se han formado en una fila por orden de llegada.
# Con el objeto de llevar registros sobre los clientes que van a la entidad bancario, el gerente necesita realizar ciertos cálculos sobre las edades de estos.
# En el banco hay 3 tipos de clientes, numerados del 1 al 3 según el tipo de cuenta que poseen.

# De cada cliente se conoce la siguiente información:
# Nombre (valor cadena)     Edad (valor entero)     Tipo_de_cliente (valor entero de 1 a 3).

# Para simplificar su trabajo, el gerente te pide que desarrolles una aplicación, que obtenga los siguientes resultados: 
# Por cada cliente, solicitar y mostrar, su nombre y su tipo de cuenta.
# Al Fnalizar, mostrar:
#     a) La cantidad de clientes en la fila, de cada tipo.
#     b) La edad del cliente más joven (se suponen únicos).
#     c) El promedio de las edades, considerando solo a los clientes del tipo 3.

tipo_cliente = int(input("Tipo de cliente (1,2,3), o 0 para finalizar: "))
cantidad_tipo1 = 0
cantidad_tipo2 = 0
cantidad_tipo3 = 0
edad = 150
edad_min = 150
total_edades = 0
promedio = 0
cliente_mas_joven = ""

while tipo_cliente < 0 or tipo_cliente > 3:
    print("Error - por favor seleccione un número del 1 al 3.")
    tipo_cliente = int(input("Elija el tipo de cliente (1,2,3): "))

while tipo_cliente != 0:
    nombre = input("Nombre del cliente: ")
    edad = int(input("Edad del cliente: "))
    while edad < 13 or edad > 150:
        print("La edad debe ser entre 13 y 150 años.")
        edad = int(input("Edad del cliente: "))
        
    if tipo_cliente == 1:
        cantidad_tipo1 += 1
    elif tipo_cliente == 2:
        cantidad_tipo2 += 1
    elif tipo_cliente == 3:
        cantidad_tipo3 += 1
        total_edades += edad
    else:
        print("Ha ocurrido un error. Por favor intente nuevamente.")

    if edad < edad_min:
        edad_min = edad
        cliente_mas_joven = nombre
    tipo_cliente = int(input("Tipo de cliente (1,2,3): "))
    
print(f"La cantidad de clientes en la fila del tipo 1 es: {cantidad_tipo1}, del tipo 2 es: {cantidad_tipo2} y del tipo 3: {cantidad_tipo3}.")
print(f"El cliente más joven es {cliente_mas_joven} con una edad de {edad_min} años.")
print(f"El promedio de edades de la categoría 3 es: {total_edades/cantidad_tipo3}")

# 3) Se realiza un censo en la provincia de Buenos Aires. Por cada persona censada se
# ingresa género (1.F, 2.M), edad y estudios cursados (1 para estudios primarios, 2
# para estudios secundarios o 3 para estudios terciarios).
# Diseñar un programa que permita ingresar los datos y calcular:
# a) Cantidad de hombres mayores a 45 años.
# b) Cantidad de mujeres encuestadas.
# c) Promedio de edad de las personas para cada tipo de estudio.
# d) Porcentaje de mujeres con estudios terciarios.
# e) Porcentaje de hombres mayores a 30 años con estudios terciarios.
# f) Promedio de edad de las mujeres mayores a 40 años con estudios
# secundarios.
# La carga de datos finaliza cuando ingresa 0 en edad y en estudios cursados.

# 4) Una empresa textil desea procesar sus ventas. Cada vez que una persona realiza una
# compra se le entrega una factura donde consta:
# • Nro. de factura
# • Código de artículo
# • Cantidad del artículo
# • Precio unitario
# En cada factura se registra solamente un código de artículo y los códigos de artículos
# pueden ser 1, 3, 5 y 7.
# Diseñar un programa que permita el ingreso de los datos y calcular:
# a) Total de cada factura
# b) Total general facturado
# c) Cantidad vendida (en unidades) para cada uno de los artículos
# d) Total de artículos vendidos
# e) Cantidad de facturas emitidas para cada uno de los artículos
# f) Nro. de factura con mayor valor (en $)
# g) Nro. de artículo con menor cantidad pedida (por factura, NO el total)
# h) Porcentaje de ventas (en pesos) de cada uno de los artículos sobre el total
# La entrada de datos finaliza con un número de factura igual a cero.

# 5) Una empresa conoce para cada empleado los siguientes datos:
# • Nombre • Sueldo • Categoría
# Hay 100 empleados, distribuidos en 3 categorías (1, 2 y 3).
# Diseñar un programa que permita ingresar los datos de todos los empleados y calcular:
# a) Total de sueldos que paga la empresa (en $)
# b) Cantidad de empleados que ganan más de $200000
# c) Cantidad de empleados que ganan menos de $500000 y cuya categoría sea 1
# d) Nombre del empleado que gana más y cuál es su sueldo
# e) Total de sueldos (en $) de cada categoría

# 6) Una empresa de mudanzas tiene 3 camiones. Cuando una persona contrata servicio, se lleva la boleta interna con los siguientes datos:
# • Nro. de viaje • Nro. de camión • Horas trabajadas • Destino (capital o interior)
# Cada camión tiene una tarifa de hora fija que es la siguiente:
# • Camión 1: 1500$ • Camión 2: 2000$ • Camión 3: 3000$
# Diseñar un programa que permita ingresar los datos de cada viaje y calcular:
# a) Total recaudado
# b) Cantidad de viajes realizados
# c) Cantidad de viajes de cada camión
# d) Cantidad de horas trabajadas de cada camión
# e) Cuántos viajes se hicieron al interior
# El ingreso de datos finaliza con nro. de viaje = 0

# 7) En un negocio de venta de chocolate hay tres tipos de chocolate: amargo, dulce y con almendras.
# El amargo cuesta $10000 el kg, el dulce $15000 y con almendras $20000 el kg. Por cada venta, ingresan al sistema:
# • Nombre del vendedor (Pedro o Pablo - se ingresa como texto)
# • Cantidad de chocolate vendido (en kg)
# • Tipo de chocolate (1. amargo, 2. dulce, 3. con almendras)
# • Día del mes (1 a 30 - nunca trabajan los 31)
# Cuando se llega a día = 31, quieren ver:
# a) Qué día del mes se registró la mayor venta (en Kg.) y quién realizó la venta.
# b) Qué día del mes se registró la mayor venta (en $) y quién realizó la venta.
# c) Quién facturó más.
# d) Cantidad de Kg. vendidos por tipo de chocolate.
# e) Porcentaje de ventas de Pedro en relación al total.

# 8) Un negocio vende empanadas y hace entregas a domicilio. Los datos que recibe el sistema son:
# • Dirección cliente
# • Cantidad de empanadas
# • Tipo de empanadas: 1. horno; 2. frita; 3. dulce.
# Las empanadas al horno cuestan $600 cada una, las fritas $580, y las dulces (de membrillo o batata) $550.
# La entrada de datos termina con cantidad de empanadas = 0. El sistema debería mostrar:
# • Dirección del cliente que más empanadas compró.
# • Cantidad de empanadas vendidas de cada tipo.
# • Mostrar la dirección de los clientes que compraron más de 15 empanadas de horno.
# • Total recaudado.
# (Considerar que cada cliente pide un solo tipo de empanada)

# 9) En una librería se venden tres tipos de artículos:
# 1. libros
# 2. artículos de escritorio
# 3. juguetes
# De cada artículo se conocen los siguientes datos:
# • Tipo de artículo
# • Precio unitario
# • Nombre del artículo
# • Cantidad en stock de cada uno
# Desarrollar un programa que permita ingresar los artículos en existencia con los correspondientes datos, finalizando la entrada de los mismos con un precio igual a cero (0).
# Además, deberá calcular:
# a) La cantidad de artículos que hay de cada tipo
# b) Cuál es el nombre del juguete más barato
# c) Cuánto dinero hay invertido en la librería
# (Inversión = Σ cantidad * precio unitario)

