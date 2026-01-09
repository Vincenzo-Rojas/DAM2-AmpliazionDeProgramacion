def alta(agenda):
	print("ALTA")
	nom=input("Introduce nombre:")
	ape=input("Introduce apellidos:")
	direc=input("Introduce direccion:")
	tel=input("Introduce telefono:")
	edad=input("Introduce edad:")
	contacto = {"nom":nom.strip(),"ape":ape.strip(),"direc":direc.strip(),"tel":tel.strip(),"edad":edad.strip()}
	if(ape in agenda.keys()):#Si ya hay un contacto con ese apellido
		if(type(agenda[ape]) is list):#Si hay mas de un contacto
			listaCon=agenda[ape]
			repe=False
			cont=0
			while(cont<len(listaCon) and not repe):
				contac=listaCon[cont]
				print("XXX",contac,tel)
				if(contac["tel"]==tel):
					repe=True
				cont+=1
					
			if(not repe):
				agenda[ape].append(contacto)
			else:
				print("Contacto repetido","No puede haber dos contactos con el mismo telefono")
		else:#Si solo hay un contacto
			if(tel==agenda[ape]["tel"]):
				print("Contacto repetido","No puede haber dos contactos con el mismo telefono")
			else:
				listaCon=[agenda[ape],contacto]
				agenda[ape]=listaCon			
	else:#Si el contacto a introducir es nuevo
		agenda[ape]=contacto
	
	
	
def baja(agenda):
	print("BAJA")
	encontrado = False
	ape=input("Introduce apellidos del contacto a borrar:")
	pos = -1
	posBorrar = -1
	for i in lista:
		pos = pos + 1
		if(i[1]==ape):
			print(i)
			encontrado = True
			opcion = input("Estas seguro de borrar? s/n ")
			if(opcion.lower()=='s' or opcion.lower()=='si'):
				posBorrar = pos
				
	if(not encontrado):
		print("Contacto no encontrado")
	else:
		if(posBorrar!=-1):
			del(lista[posBorrar])
			print("Contacto borrado")
	
def modificacion(agenda):
	print("MODIFICAR")
	encontrado = False
	ape=input("Introduce apellidos del contacto a modificar:")
	pos = -1
	posBorrar = -1
	for i in lista:
		pos = pos + 1
		if(i[1]==ape):
			print(i)
			encontrado = True
			newtel = input("Introduce el nuevo telefono:")
			opcion = input("Estas seguro de modificar? s/n ")
			if(opcion.lower()=='s' or opcion.lower()=='si'):
				i[3]=newtel
				print("Contacto modificado")
				
	if(not encontrado):
		print("Contacto no encontrado")

	
def buscar(agenda):
	print("BUSCAR")
	ape=input("Introduce apellidos del contacto a buscar:")
	if(ape in agenda.keys()):
		contac = agenda[ape]
		if(isinstance(contac,list)):
			for j in contac:
				print("\t",j)
		else:
			print(i)
	else:
		print("Contacto no encontrado")
		
	
def mostrar(agenda):
	print("\n\n------------")
	print("-- AGENDA --")
	print("------------\n")
	for i in agenda.values():
		if(isinstance(i,list)):
			for j in i:
				print("\t",j)
		else:
			print(i)
	
def menu():
	print("\n********")
	print("* MENU *")
	print("********")
	print("1.Alta")
	print("2.Baja")
	print("3.Modificacion")
	print("4.Busqueda")
	print("5.Mostrar")
	print("0.Salir")
	opcion = input("Introduce opcion:")
	return opcion
	
print("Empezamos agenda listas")
agenda={}
salir=False
while(not salir):
	opcion=menu()
	if(opcion=='1'):
		alta(agenda)
	elif(opcion=='2'):
		baja(agenda)
	elif(opcion=='3'):
		modificacion(agenda)
	elif(opcion=='4'):
		buscar(agenda)
	elif(opcion=='5'):
		mostrar(agenda)
	elif(opcion=='0'):
		print("Terminamos")
		salir=True
	else:
		print("Opcion no valida")

print("Fin agenda listas")
