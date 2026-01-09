def ejem1():
	dic={}
	dic2={1:'a',2:'b','3':[1,2,3]}
	print(dic2['3'][2],"**********")
	print(dic2[1])
	dic2[1]='c'
	print(dic2[1])
	#print(dic2[0]) #ERROR
	dic2[4]='f'
	print(dic2)
	del(dic2['3'])
	print(dic2)
	print(dic2.keys())
	print(dic2.values())
	print(dic2.items())
	
def ejer1():
	dic={'a':1,'b':2,'c':3,'d':4}
	for i in dic.keys():
		print(i,dic[i])
	print("OTRA FORMA")
	for i in dic.items():
		print(i[0],i[1],type(i))

def contar(cadena,encontrar):
	veces=0
	posicion=0
	posicion=cadena.find(encontrar)
	while(posicion!=-1):
		veces+=1
		posicion=cadena.find(encontrar, posicion+1, len(cadena))
	return veces
	
def contar2(cadena,encontrar):
	veces=0
	posicion=0
	posicion=cadena.find(encontrar)
	while(posicion!=-1):
		veces+=1
		posicion=cadena.find(encontrar, posicion+1)
	return veces

def ejem2_cadenas():
	cadena = "Bienvenido a mi aplicacion"
	print(cadena.upper())
	cadena = cadena.upper()
	print(cadena)
	
	cadena = "bienvenido a mi aplicacion"
	print(cadena.find("mi") )
	print(cadena.find("mi", 0, 10) )
	
	cadena = "cadena de prueba"
	encontrar="de"
	
	


print("Empezamos")

#ejem1()
#ejer1()
#ejem2_cadenas()
print(contar2("cadena de prueba de examen de","de"))

dic2={"ortiz":{},"garcia":[{},{}]}

print("ortiz" in dic2.keys())
print("martin" in dic2.keys())

print("Fin")
