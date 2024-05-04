# Una empresa se dedica a encuestar personas y para ello necesita ingresar los datos
# de sus encuestados mediante un programa. Los datos de entrada que se solicitan
# cargar son:
# • Tipo de encuesta realizada (1- Telefónica, 2- Presencial).
# • Documento de la persona encuestada
# • Género de la persona encuestada (M/F).
# • Cantidad de hijos de la persona encuestada y edades de los mismos.
# La carga de datos finaliza cuando en el tipo de la encuesta se lee "FIN". Al finalizar el
# proceso, el programa debe mostrar por pantalla:
# a) Porcentaje de encuestados por cada tipo de encuesta.
# b) Si el género es "M" y tiene más de 2 hijos, promediar las edades de los mismos.
# c) Cual fue el grupo personas que más se encuesto según su género.
# d) El documento de la persona encuestada que tiene el hijo de mayor edad.

encuestasF = 0
encuestasM = 0
encuesta_1 = 0
encuesta_2 = 0
min_hijos = 0
min_doc = 0
encuesta = int(input("Ingrese el número de encuesta: "))

while encuesta > 2 or encuesta < 0:
    encuesta = int(input("Error. Ingrese el número de encuesta (0-2): "))
while encuesta != 0:
    documento = int(input("Ingrese el número de documento: "))
    while documento < 0:
        documento = int(input("Error. Ingrese el número de documento: "))
    sexo = input("Ingrese el sexo del encuestado(M/F): ")
    while sexo != "M" and sexo != "F":
        sexo = input("Error. Ingrese el sexo del encuestado(M/F): ")
    cantHijos = int(input("Ingrese la cantidad de hijos: "))
    while cantHijos < 0:
        cantHijos = int(input("Error. Ingrese la cantidad de hijos: "))

if encuesta == 1:
    encuesta_1 += 1
else:
    encuesta_2 += 1

if sexo == "M":
    encuestasM += 1
else:
    encuestasF += 1

if cantHijos > 1:
    sumaEdades = 0
    for i in range(cantHijos):
        edad = int(input("Ingrese la edad de cada hijo: "))
        while edad < 0:
            edad = int(input("Ingrese la edad de cada hijo: "))
        sumaEdades += edad
        print("El promedio de edades del encuestado es: ", sumaEdades/cantHijos)
else:
    encuestasF += 1