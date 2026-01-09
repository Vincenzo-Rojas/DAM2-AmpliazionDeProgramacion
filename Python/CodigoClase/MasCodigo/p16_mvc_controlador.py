import p16_mvc_vista

def alta(lista):        
    contacto = p16_mvc_vista.alta()
    lista.append(contacto)
        
        
def baja(lista):
    ape=p16_mvc_vista.bajaPedirApe()
    encontrado = False
    pos = -1
    posBorrar = -1
    for i in lista:
        pos = pos + 1
        if(i[1]==ape):
            p16_mvc_vista.bajaMostrarContacto(i)
            encontrado = True
            opcion = p16_mvc_vista.bajaMsgConfirmacion()
            if(opcion.lower()=='s' or opcion.lower()=='si'):
                posBorrar = pos
                                
    if(not encontrado):
        p16_mvc_vista.bajaMsgNoEncontrado()
    else:
        if(posBorrar!=-1):
            del(lista[posBorrar])
            p16_mvc_vista.bajaMsgBorrado()
        
def modificacion(lista):
    ape=p16_mvc_vista.modPedirApe()
    encontrado = False
    pos = -1
    posBorrar = -1
    for i in lista:
        pos = pos + 1
        if(i[1]==ape):
            p16_mvc_vista.modMostrarContacto(i)
            encontrado = True
            newtel = p16_mvc_vista.modNuevoTelefono()
            opcion = p16_mvc_vista.modMsgConfirmacion()
            if(opcion.lower()=='s' or opcion.lower()=='si'):
                i[3]=newtel
                p16_mvc_vista.modMsgModificado()
                                
    if(not encontrado):
        p16_mvc_vista.modMsgNoEncontrado()

        
def buscar(lista):
    ape=p16_mvc_vista.busPedirApe()
    encontrado = False
    for i in lista:
        if(i[1]==ape):
            p16_mvc_vista.busMostrarContacto(i)
            encontrado = True
    if(not encontrado):
        p16_mvc_vista.busMsgNoEncontrado()
        

p16_mvc_vista.mensajeIniProg()
        
agenda=[]
salir=False
while(not salir):
    opcion = p16_mvc_vista.menu()
    if(opcion=='1'):
        alta(agenda)
    elif(opcion=='2'):
        baja(agenda)
    elif(opcion=='3'):
        modificacion(agenda)
    elif(opcion=='4'):
        buscar(agenda)
    elif(opcion=='5'):
        p16_mvc_vista.mostrar(agenda)
    elif(opcion=='0'):
        p16_mvc_vista.msgTerminar()
        salir=True
    else:
        p16_mvc_vista.msgOpcionNoValida()

p16_mvc_vista.mensajeIniProg()

