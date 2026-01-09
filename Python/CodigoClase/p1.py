print("Hola mundo")

a = 5
print(a)
a="Cadena"
print(a)
a='Cad""ena2'
print(a)

print(a,"->",type(a))
a = 5
print(a,"->",type(a))
a = 5.6
print(a,"->",type(a))

cadena = "aaa"+"bbb"
print(cadena)
print(cadena+str(a))

entrada = input("Introduce un numero:")
print(entrada)
print(entrada,type(entrada))

entrada = int(input("222. Introduce un numero:"))
print(entrada)
print(entrada,type(entrada))

if(entrada>10):
	print("Es mayor que 10")
elif(entrada>=0):
	print("Mayor que 0 y menor o igual que 10")
else:
	print("Menor que 0")

print("Esto esta fuera del if")

#Esto es un comentario de una linea

'''
Esto es un comentario de varias
lineas
'''

n1 = int(input("Introduce num1:"))
n2 = int(input("Introduce num2:"))
ope = input("Introduce operacion: (+,-,*,/) ")
if(ope == "+"):
	print("La suma es:",n1+n2)
elif(ope == "-"):
	print("La resta es:",n1-n2)
elif(ope == "*"):
	print("La multiplicacion es:",n1*n2)
elif(ope == "/"):
	print("La division es:",n1/n2)
else:
	print("Operacion no valida")
	
cont=1
while(cont<10):
	print(cont)
	cont=cont+1

#Ejercicio. Un programa que pida un numero y muestre la tabla de multiplicar
# de dicho numero

n1 = int(input("Introduce un numero:"))
cont=1
while(cont<=10):
	print(n1,"*",cont,"=",n1*cont)
	cont=cont+1
	
#Ejercicio. Un programa que pida un numero e indique si el numero es o no primo


print("Fin")
