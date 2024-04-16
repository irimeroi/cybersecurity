# Ingresar las edades de 50 empleados de una empresa. Determinar la diferencia entre la edad máxima y la edad mínima y mostrarla.
edades_empleados = [28, 35, 42, 19, 51, 46, 33, 25, 39, 55, 30, 22, 48, 37, 29, 43, 26, 36, 50, 31, 24, 45, 52, 27, 38, 41, 32, 47, 21, 53, 40, 34, 49, 23, 44, 56, 20, 54, 18, 59, 63, 57, 61, 58, 60, 64, 22, 68, 65, 62]
maximo = edades_empleados[0]
minimo  = edades_empleados[0]

for edad in edades_empleados:
    if edad > maximo:
        maximo = edad
    if edad < minimo:
        minimo = edad
print(f"La diferencia entre la edad mínima y máxima es: {maximo - minimo}")

# Ingresar las temperaturas registradas a distintas horas de un día en grados hasta que esta sea 100. Mostrar la temperatura máxima y la temperatura mínima.
temp_maxima = 0
temp_minima = 100

while True:
    temperaturas = int(input("Ingresar temperaturas del día: "))
    if temperaturas > temp_maxima:
        temp_maxima = temperaturas
    if temperaturas < temp_minima:
        temp_minima = temperaturas
    if temperaturas >= 100:
        break
print(f"La temperatura mínima del día fue: {temp_minima}")
print(f"La temperatura máxima del día fue: {temp_maxima}")

temperaturas = []
while True:
    input_temp = int(input("Ingresar temperaruras: "))
    if input_temp == 100:
        break
    temperaturas.append(input_temp)

    maxima_temp = temperaturas[0]
    minima_temp = temperaturas[0]
    for temp in temperaturas:
        if input_temp > maxima_temp:
            maxima_temp = input_temp
        if input_temp < minima_temp:
            minima_temp = input_temp
print(f"La temperatura mínima del día fue: {minima_temp}")
print(f"La temperatura máxima del día fue: {maxima_temp}")

