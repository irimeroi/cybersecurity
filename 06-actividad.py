# Una cadena de hoteles cuenta con 10 filiales y necesita obtener algunas estadísticas para mejorar sus servicios. Para ello se ingresan:

# Nombre de la ciudad de la filial
# Capacidad total del hotel (en cuanto a huéspedes)
# Cantidad de habitaciones
# Cantidad de huéspedes en un mes.
# Calcular y mostrar:

# Cantidad de huéspedes que puede alojar toda la cadena de hoteles
# Porcentaje de ocupación de cada hotel.
# El nombre de la ciudad con la mayor cantidad de habitaciones. 

capacidad_total_cadenas = 0
total_filiales = 10
max_habitaciones = 0

for i in range(total_filiales):
    ciudad = input("Ingrese el nombre de la ciudad de la filial de esta cadena de hoteles: ")
    
    # calcula la cantidad de huéspedes que puede alojar toda la cadena de hoteles
    capacidad_total_hotel = int(input("Ingrese capacidad total de huespedes: "))
    while capacidad_total_hotel <= 0:
        capacidad_total_hotel = int(input("Número erróneo. Por favor ingrese un número entero mayor a 0: "))
    capacidad_total_cadenas += capacidad_total_hotel

    # devuelve el nombre de la ciudad con la mayor cantidad de habitaciones.
    cantidad_habitaciones = int(input("Ingrese la cantidad de habitaciones que tiene el hotel: "))
    while cantidad_habitaciones <= 0:
        cantidad_habitaciones = int(input("Número erróneo. Por favor ingrese un número entero mayor a 0: "))

    if cantidad_habitaciones > max_habitaciones:
        max_habitaciones = cantidad_habitaciones
        ciudad_mas_habitaciones = ciudad

    # calcula el porcentaje de ocupación de cada hotel.
    huespedes_por_mes = int(input("Ingrese la cantidad de huéspedes en un mes: "))
    while True:
        if huespedes_por_mes <= 0:
            huespedes_por_mes = int(input("Número erróneo. Por favor ingrese un número entero mayor o igual a 0: "))
        elif huespedes_por_mes > capacidad_total_hotel:
            huespedes_por_mes = int(input("Número erróneo. La cantidad de huéspedes por mes debe ser menor a la capacidad máxima de huéspedes: "))
        else:
            print ("El porcentaje de ocupación del hotel de", ciudad, "es del", huespedes_por_mes * 100 / capacidad_total_hotel, "%")
            break

print("La cantidad de huéspedes que puede alojar la cadena de hoteles es de", capacidad_total_cadenas, "personas.")
print("La ciudad con mayor cantidad de habitaciones es", ciudad_mas_habitaciones ,"contando con", max_habitaciones,"habitaciones.")