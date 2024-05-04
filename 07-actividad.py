# Un dentista de la zona le solicitó que realice un programa para poder llevar su agenda de turnos.
# En el mismo debe existir un menú para que la secretaria pueda realizar sus tareas con facilidad, ya que según lo que ella misma informa "la computadora no es su amiga". En el menú deben visualizarse las siguientes opciones:

# Ingresar turnos
# Ver turnos
# Eliminar turnos cancelados
# Ver estadísticas
# Salir
# En cada ítem del menú deberá:

# Ingresar turnos: El dr. solo atiende 23 pacientes por día, los datos que se registran de cada paciente son los siguientes:
# Nombre
# Número de socio
# Horario(de 8 a 20hs)
# Tratamiento (Control, arreglo de caries, ortodoncia, extracción) 
# Ver turnos: debe mostrar todos los turnos ordenados de menor a mayor según el horario asignado mostrando todos los datos de cada paciente en forma prolija y clara.
# Eliminar turnos: si un cliente llama para eliminar el turno, la secretaria le pedirá su número de socio y eliminará el turno.
# Ver estadísticas:
# Promedio de todos los pacientes que se realizan ortodoncia
# Cantidad de pacientes a atender antes de las 16hs

user_input = int(input("Elija una opción: \n1. Ingresar turnos \n2. Ver turnos \n3. Eliminar turnos cancelados \n4. Ver estadísticas \n5. Salir"))
cantidad_pacientes = 2

if user_input == 1: 
    nombre = input("Ingrese el nombre del paciente: ")
    socio = input("Ingrese el número de socio: ")
    horario = input("Ingrese el horario del turno: ")
    tratamiento = input("Ingrese el tratamiento (Control, arreglo de caries, ortodoncia, extracción): ")
paciente = nombre, socio, horario, tratamiento
print(paciente)
