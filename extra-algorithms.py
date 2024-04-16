# 04 - MAX AND MIN ALGORITHMS
# Por cada alumno de la facultad se dispone de la siguiente información:• Número de legajo• Nota promedio de finales rendidos
# a) Ingresar estos datos hasta que el número de legajo sea cero.
# b) Determinar los números de legajo de los dos mejores promedios. c) Mostrarlos.

#-----------------------------------------------------------------
# Del censo realizado en una población se conocen los siguientes datos:
# • Día de nacimiento (2 dígitos)• Mes de nacimiento (2 dígitos)• Año de nacimiento (4 dígitos)• Género (‘M’: masculino / ‘F’: femenino)
# Ingresar estos datos hasta que el día de nacimiento sea cero. Calcular y mostrar:
# a) Cuántos nacimientos hubo en el mes de octubre de todos los años.
# b) Cuántos nacimientos hubo antes del 9 de julio de 1970.
# c) Cuántos nacimientos de mujeres hubo en la primavera de 1942.
# d) Género de la persona más anciana (solo existe una)

#-----------------------------------------------------------------
# El gobierno de la Ciudad de Buenos Aires realiza una encuesta en casas de familia.
# De cada familia conoce: domicilio, tipo de vivienda (‘C’: casa, ‘D’: departamento), y cantidad de integrantes.
# De cada integrante de la familia se conoce: nombre y apellido, edad, género (‘F’,‘M’),
# nivel de estudios alcanzados (‘N’: no posee, ‘P’: primario, ‘S’: secundario, ‘T’: terciario, ‘U’: universitario),
# y un indicador (‘I’: incompleto, ‘C’: completo) que serefiere al ítem anterior.
# Los datos finalizan cuando la cantidad de integrantes sea igual a cero.
# Se pide calcular:
# a) El porcentaje de analfabetismo en la ciudad (se considera analfabetos a losmayores de 10 años que no posean estudios).
# b) El domicilio de la familia con mayor cantidad de integrantes que viven endepartamento.
# c) Edad promedio de cada familia.
# d) Cantidad de encuestados en cada tipo de nivel de estudios alcanzadosincompletos.
# e) Porcentaje de encuestados de género femenino y masculino.

#-----------------------------------------------------------------
# Una aerolínea decide sacar a la venta en promoción pasajes con destino a 3 provincias poco visitadas del país, por un valor de 25500 pesos el pasaje,
# y le solicitaron que realice un programa para llevar el control de los viajes vendidos.
# Los datos que se ingresan al momento de la compra son:
# • Lugar de destino (Neuquén, Tucumán o Salta) • Cantidad de pasajes • Número de factura
# a) Se desea saber cuál es el destino que recibirá mayor cantidad de turistas.
# b) Quién fue el comprador que más pasajes compró en una misma factura. (Solo secomprará un destino por factura) Ej.: Salta, 5 pasajes, factura 198.
# Se debe tener en cuenta que el operador es nuevo en la empresa, por lo que no debe permitir que ingrese cantidad de pasajes negativos, ni venda promociones a otrasprovincias fuera de las mencionadas.

#-----------------------------------------------------------------
# Se decide jugar un juego de tiro al blanco y llevar el control de los puntos con un algoritmo que desarrollarás para tal fin.
# Cada jugador tendrá un total de 3 tiros en los que podrá obtener los siguientes puntajes:
# • Sector doble: Los pequeños sectores más al extremo de la diana, puntúan el doble del número que representan.
# Si el dardo va a parar aquí obtendremos 6 x 2 = 12 puntos.
# • Sectores simples: estos sectores más grandes puntúan el mismo valor del número.
# Si el dardo va a parar al sector b o d, sumaremos 6 puntos.
# • Sector triple: Los sectores pequeños del medio del radio de la diana puntúan el triple del número representado.
# En este caso puntuaría 6 x 3 = 18 puntos.
# • El sector exterior del centro de la diana puntúa 25 puntos
# • El sector interior del centro de la diana puntúa 50 puntos.

# Al comenzar el juego se pedirá que se ingrese: el número de jugador, valor de cada tiro y si el mismo es simple, doble o triple.
# Se ingresarán datos hasta que el número de jugador seaigual a cero.
# • Se pide calcular el ganador de la partida. Siendo el ganador aquel que sacó mayor cantidad de puntos. Mostrar puntos y número de jugador.
# • Se debe validar el ingreso de los puntos. (0- fuera, 1 a 20, 25 o 50)
# • El número del jugador con menor cantidad de puntos

#-----------------------------------------------------------------
# Se ponen a la venta las entradas para un partido de fútbol internacional, cuyo precio depende de la tribuna elegida:
# • Tribuna norte y sur cuestan 8500 pesos.
# • Tribuna este y oeste cuesta 7500 pesos.
# Cada persona podrá comprar la cantidad de entradas que desee, pero siempre en la misma tribuna.
# Los datos que se deben ingresar son el nombre del comprador y la cantidad de entradas compradas. (Cantidad de entradas no podrá ser negativa.)
# Finaliza la carga cuando el operador lo determine.
# Diseñe un programa que controle la venta de dichas entradas a fin de poder saber:
# a) La cantidad de personas que asisten a cada tribuna.
# b) La cantidad total de personas y el monto total recaudado por la venta de todas lasentradas.
# c) La persona que compró mayor cantidad de entradas