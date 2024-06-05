# Leer números hasta cargar un arreglo A con 14 elementos donde los 7 primeros  elementos deben ser pares y los 7 restantes, impares.

# Mostrarlo.
# Generar otro arreglo poniendo los elementos pares del arreglo A en las posiciones pares del arreglo B y los elementos impares del arreglo A en las posiciones impares del arreglo B. Mostrarlo.
# Ordenar el segundo arreglo de mayor a menor desde la posición del primer múltiplo de 4. Si no lo hubiese, mostrar un cartel aclaratorio.
# Números leídos: 10,15,12,135,46,845,124,78,35,17,48,49,23,56

def mostrar (vec,n):
   for i in range(0,n):
       print(vec[i])
 
def cargar(pares,impares,n):
   i=0
   j=0
   while i < 7 or j < 7:
       num=int(input("ingrese un numero"))
       if num % 2==0 and i < 7:
           pares.append(num)
           i+=1
       if num % 2 !=0 and j < 7:
           impares.append(num)
           j+=1
   return
 
def generar(vec,b):
   i=0
   j=0
   while i< 7:
       b[j]=vec[i]
       b[j+1]=vec[i+7]
       i+=1
       j+=2
   return
 
def buscar(b):
   i=0
   while i <14 and b[i]%4!=0:
       i=i+1
   return i
 
def ordenar(b,pos):
   for i in range(pos,14):
       for j in range(i+1,14):
           if b[i]>b[j]:
               aux=b[i]
               b[i]=b[j]
               b[j]=aux
   return 

longitud =14
pares=[]
impares=[]
vec=[]
b=[]
for i in range(0,14):
   b.append(0)
cargar(pares, impares,longitud)
print("El arreglo de pares")
mostrar(pares,7)
print("El arreglo de impares")
mostrar(impares,7)
vec=pares+impares
mostrar(vec,14)
generar(vec,b)
print("intercalado")
mostrar(b,14)
pos=buscar(b)
if pos==14:
   print("no hay multiplo de 14")
else:
   ordenar(b,pos)
print("El arreglo ordenado")
mostrar(b,14)