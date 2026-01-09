print("Empezamos diccionarios")


#Crear
dic={} #utilizando llaves
dic2={1:'a',2:'b'}
print(dic2)

#Lectura
print(dic2[1])

#Modificacion
dic2[1]='c'
print(dic2[1])

# print(dic2[0]) ERROR porque no existe clave '0'

dic2[3]='d'
print(dic2)

#Borrar
del(dic2[1]) #un elemento
print(dic2) #todo el diccionario

dic={1:'a',2:'b'}
print(dic.keys())

print(dic.values())
for i in dic.values():
    print(i)

print("*"*25)
for i in dic.items():
    print(i,type(i))
        

'''
Contacto:
Nombre
Apellidos
Direccion
Telefono
Edad

Agenda
1.Alta
2.Borrar
3.Modificar
4.Buscar
5.Mostrar todos
0.Salir
Introduce opcion:
'''

print("Fin diccionarios")
