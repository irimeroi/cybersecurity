# Ingresar números hasta un múltiplo de 3. Mostrar el último número ingresado.
while True:
    nums = int(input("Ingresar números del 1 a 10. El programa se va a cerrar cuando ingrese un múltiplo de 3."))
    if nums % 3 == 0:
        print(str(nums) + " es múltiplo de 3!")
        break
    else:
        print("Por favor ingrese un número válido")

# Calcular el promedio semanal de gastos en un mes, ingresando como datos:• Semana número• Gasto semanal
semanas = 0
gastos = 0

while True:
    if semanas == 4:
        break
    gasto_semanal = float(input("Gasto semanal: "))
    gastos += gasto_semanal
    semanas += 1
promedio_gastos = gastos/semanas
print(promedio_gastos)

# Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo de cada curso:
# Curso (1-5) - Presentes - Ausentes
# Calcular:• Por cada curso el porcentaje de presentes sobre el total• Cantidad de ausentes en el colegio
total_ausentes = 0
cursos = 5

for curso in range(1, cursos+1):
    print(f"\nCurso número: {curso}")
    try:
        presentes = int(input("Ingrese la cantidad de alumnos presentes: "))
        ausentes = int(input("Ingrese la cantidad de alumnos ausentes: "))
    except ValueError:
        print("Ingresar un número válido")
    
    total_colegio = presentes + ausentes
    if total_ausentes == 0:
        print("El total no puede ser 0.")
    porcentaje_presencias = (presentes/total_colegio)*100
    print(f"El porcentaje de presencias es de: {porcentaje_presencias:.2f}%")

    total_ausentes+= ausentes
print(f"La cantidad de ausentes en el colegio el día de hoy es: {total_ausentes}")


# Leer el número de mes y mostrar cuántos días tiene ese mes (año actual).
import datetime

anio_actual = datetime.datetime.now().year
es_bisiesto = (anio_actual%4 == 0 and anio_actual%100 != 0) or (anio_actual%400 == 0)
meses = 12

for mes in range(1, meses+1):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print(f"\n El mes {mes} tiene 31 días")
    elif mes == 2 and es_bisiesto:
        print(f"\n El mes {mes} tiene 29 días")
    elif mes == 2:
        print(f"\n El mes {mes} tiene 28 días")
    else:
        print(f"\n El mes {mes} tiene 30 días")

# Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.
print("Ingresar números enteros. Al ingresar el número 0, el programa te dirá cuántos son positivos")
numeros_positivos = 0
numeros = None

while numeros != 0:
    try:
        numeros = int(input("Ingresar números: "))
        if numeros > 0:
            numeros_positivos += 1
    except ValueError:
        print("Número o caracter inválido")
print(f"La cantidad de números positivos es: {numeros_positivos}")

# Ingresar 10 números mayores a 3 y menores a 8. Mostrar el valor ingresado en número y letras.

# Leer dos números, mostrar el siguiente menú pudiendo seleccionar alguna opción yrepetir esta operación hasta que seleccione 5
# Menú principal 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. SalirSeleccione una opción

# Leer un número y calcular la suma de los números naturales hasta ese número. Modificar el algoritmo para que pueda procesar muchos números. Dar por terminada la entrada cuando el número sea 0.

# Escribir un algoritmo que encuentre los dos primeros números perfectos. Un número perfecto es un entero positivo, que es igual a la suma de todos los enteros positivos (excluido el mismo) que son divisores del número.
# El primer número perfecto es 6, ya que lo divisores de 6 son 1, 2, 3 y 1 + 2 + 3 = 6.