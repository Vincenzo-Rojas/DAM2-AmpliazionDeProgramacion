print("Comienza")

print("Prueba sin salto de linea", end="")
print("Prueba sin salto de linea", end="")
print()
print("Prueba sin salto de linea")

double = 5.000009

print(double)

print()

#mostrar los numeros del 10 al 1 en ese orden

for i in range(10,0,-1):
	print(i)

num = int(input("Dime un numero y te dire su tabla de multiplicar: "))
for	i in range(11):
	print(i*num)

for i in range(num, num*11, num):#inicio, maximo, pasos
	print(i)

t1 = 1, "a", [9,1,3]
print("Saca la pos 2 de la lista de t1")
print(t1[2][1])


#lista 1 a 10
print("lista 1 a 10")
lista=[]
for i in range (1,11,1):
	lista.append(i)
print(lista) #len(lista)

num = int(input("Indica un numero para desplazar, positivo hacia la drch y negativo hacia la izq. El numero representa la cantidad de deplazamientos:  "))


#if(num == 0): # no hay desplazamiento
if(num > 0): # desplazar derecha
	for i in range (num):
		temp = lista.pop()
		lista.insert(0,temp)
				
if(num < 0): # desplazar izquierda
	for i in range (-num):	
		temp = lista[0]
		del(lista[0])
		lista.append(temp)
		
print(lista)
