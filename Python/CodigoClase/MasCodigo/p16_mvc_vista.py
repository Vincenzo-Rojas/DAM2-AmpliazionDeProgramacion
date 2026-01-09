print("p16_mvc_vista")


def mensajeIniProg():
    print("Empezamos agenda listas MVC")
    
def mensajeFinProg():
    print("Fin agenda listas MVC")
    
def msgTerminar():
    print("Terminamos")
    
def msgOpcionNoValida():
    print("Opcion no valida")

#ALTA
def alta():
    print("ALTA")
    nom=input("Introduce nombre:")
    ape=input("Introduce apellidos:")
    direc=input("Introduce direccion:")
    tel=input("Introduce telefono:")
    edad=input("Introduce edad:")
    contacto = [nom,ape,direc,tel,edad]
    return contacto
#ALTA

#BAJA			
def bajaPedirApe():
    print("BAJA")
    ape=input("Introduce apellidos del contacto a borrar:")
    return ape

def bajaMostrarContacto(contacto):
    print("Contacto a borrar:",contacto)
    
def bajaMsgConfirmacion():
    opcion = input("Estas seguro de borrar? s/n ")
    return opcion

def bajaMsgNoEncontrado():
    print("Contacto no encontrado")

def bajaMsgBorrado():
    print("Contacto borrado")

#BAJA

#MODIFICAR
def modPedirApe():
    print("MODIFICAR")
    ape=input("Introduce apellidos del contacto a modificar:")
    return ape

def modMostrarContacto(contacto):
    print("Contacto a modificar:",contacto)
    
def modNuevoTelefono():
    tel = input("Introduce el nuevo telefono:")
    return tel    
    
def modMsgConfirmacion():
    opcion = input("Estas seguro de modificar? s/n ")
    return opcion

def modMsgNoEncontrado():
    print("Contacto no encontrado")

def modMsgModificado():
    print("Contacto modificado")
#MODIFICAR

#BUSCAR
def busPedirApe():
    print("BUSCAR")    
    ape=input("Introduce apellidos del contacto a buscar:")
    return ape

def busMostrarContacto(contacto):
    print("Contacto:",contacto)

def busMsgNoEncontrado():
    print("Contacto no encontrado")    
#BUSCAR


def mostrar(lista):
    print("\n\n------------")
    print("-- AGENDA --")
    print("------------\n")
    for i in lista:
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
