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
