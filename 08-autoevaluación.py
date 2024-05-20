a=[]
b=int (input("Ingrese un numero"))
for i in range (1,b):
  if b%i==0:
      a.append(i)
print(a) 


a=[]
b=int (input("Ingrese un numero"))
for i in range (1,b):
  if b%i==0:
      a.append(i)
a.reverse()      
print(a)  


a=[0,0,0,0,0]
for i in range (0,5):
   for j in range (1,6):
       a[i]=a[i]+j
print(a) 


a = []
b = []
num = int (input("ingresar un número"))
while(num>0):
   if(num%2 == 0):
       a.append(num)
   else:
       b.append(num)
if (len(a) > len (b)):
   for i in range(0, len(a)):
       print(a[i])
else:
   for i in range (0, len(b)):
       print(b[i])


a=[]
b=int (input("Ingrese un numero"))
while b > 0:
   if b%2==0 and b%5!=0:
      a.append(b)
   b=int (input("Ingrese un numero")) 
a.sort()      
print(a) 
