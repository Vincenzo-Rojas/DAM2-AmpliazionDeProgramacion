print("Empezamos")




# esto es una cadena
c = "Hola Mundo"
print(type(c))
# y esto es un entero
c = 23
# podemos comprobarlo con la función type
print(type(c))

num = input("Introduce un numero: ")
print(type(num))

num = int(num)
print(type(num))

num2 = int(input("Introduce otro numero: "))
print(type(num2))
print("*"*25)

print("*"+str(25))

#print("*"+25)
print("*",25)

for i in range(1,11):
	print(i)
	
print("*",25)

for i in range(11,1,-2):
	print(i)
	
cadena="cadena de prueba"
for i in cadena:
	print(i)
	
print("Fin")
