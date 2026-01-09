import random

print("Empezamos")

def ejer1():
	print("Ejer1")
	t1=(1,2,'a',("as",'ty'),True)
	lista = []
	for i in t1:
		lista.append(i)
	print(lista)
	
def ejer2(longi,rango):
	print("Ejer2")
	lista=[]
	for _ in range(longi):
		num = random.randint(1,rango)
		while(num in lista):
			num = random.randint(1,rango)
		lista.append(num)
	return lista
		
	
print("Tuplas")
t1=(1,2,3,"asd",(1,5,7))
print(t1[2])
print(t1[4],t1[4][1])
#t1[0] = 7

t2=1,2,3,"asd",(1,5,7)
print(t2[3])

print("*"*25)
print(t2)
print(t2[1:3])
print(t2[1:5])
print(t2[1:5:2])
print(t2[5:1:-1])

for i in t2:
	print(i)
	
print("LISTAS")

ListaEstaciones = ['Invierno', 'Primavera',"Verano", "Otonyo"] # Declara lista


lista = [22, True, 'una lista', [1, 2]]
print(lista[-1][1])
print(lista[-1][-1])
print(len(lista),"longitud de la lista")
lista=[22, False]
lista[0]=54
print(lista)
#lista[2]=5 # ERROR. NO SIRVE PARA ANYADIR

#ejer1()
print(ejer2(5,10))
print(ejer2(5,5))
print(ejer2(10,10))

print("Fin")
