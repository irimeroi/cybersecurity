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

