import p17_mvc_vista
import p17_mvc_modelo

def alta():        
    contacto = p17_mvc_vista.alta()
    p17_mvc_modelo.alta(contacto)
        
        
def baja():
    ape=p17_mvc_vista.bajaPedirApe()
    contacto,pos = p17_mvc_modelo.buscar(ape)
    if(contacto!=None):
        p17_mvc_vista.bajaMostrarContacto(contacto)
        opcion = p17_mvc_vista.bajaMsgConfirmacion()
        if(opcion.lower()=='s' or opcion.lower()=='si'):
            p17_mvc_modelo.borrar(pos)
    else:
        p17_mvc_vista.bajaMsgNoEncontrado()
        
    
        

        

p17_mvc_vista.mensajeIniProg()
        
salir=False
while(not salir):
    opcion = p17_mvc_vista.menu()
    if(opcion=='1'):
        alta()
    elif(opcion=='2'):
        baja()
    elif(opcion=='3'):
        pass#modificacion(agenda)
    elif(opcion=='4'):
        pass#buscar(agenda)
    elif(opcion=='5'):
        agenda = p17_mvc_modelo.mostrar()
        p17_mvc_vista.mostrar(agenda)
    elif(opcion=='0'):
        p17_mvc_vista.msgTerminar()
        salir=True
    else:
        p17_mvc_vista.msgOpcionNoValida()

p17_mvc_vista.mensajeIniProg()

