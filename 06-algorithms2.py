
# b) Calcular el total de sueldos que paga la empresa.
# c) Determinar cuántos empleados de cada categoría hay.

comenzar = input("Desea comenzar a agregar empleados? (Y/N)")
categoria1 = 0
categoria2 = 0
categoria3 = 0
categoria4 = 0

while comenzar == "Y":
    categoria = int(input("Ingrese la categoría (1, 2, 3 o 4). 0 para terminar: "))

    if categoria < 1 or categoria > 4:
        print("Por favor ingrese un número del 1 al 4: ")
    else:
        if categoria == 1:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 4500
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
        elif categoria == 2:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 5000
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
        elif categoria == 3:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 5500
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
        elif categoria == 4:
            horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            sueldo_bruto = horas_trabajadas * 5800
            sueldo_neto = sueldo_bruto - (sueldo_bruto*17/100)
            print("El sueldo bruto del empleado es: ", sueldo_bruto, "y el sueldo neto es: ", sueldo_neto)
        else:
            print("Ha habido un error, por favor intente nuevamente")    

print("La cantidad de empleados en la categoría 1 es: ", categoria1)
print("La cantidad de empleados en la categoría 2 es: ", categoria2)
print("La cantidad de empleados en la categoría 3 es: ", categoria3)
print("La cantidad de empleados en la categoría 4 es: ", categoria4)