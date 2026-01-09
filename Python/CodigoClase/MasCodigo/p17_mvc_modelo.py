agenda = []

def alta(contacto):
    agenda.append(contacto)

def buscar(ape):
    encontrado = False
    pos = -1
    posBorrar = -1
    for i in agenda:
        pos = pos + 1
        if(i[1]==ape):
            return i,pos
    return None,None
    
def borrar(pos):
    del(agenda[pos])
    
def borrar2(ape):
    encontrado = False
    pos = -1
    posBorrar = -1
    for i in agenda:
        pos = pos + 1
        if(i[1]==ape):
            del(agenda[pos])
            return i
    return None

def mostrar():
    return agenda
