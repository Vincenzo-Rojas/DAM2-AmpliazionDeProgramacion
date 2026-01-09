import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

def leerXML(fichero):
    root = None
    try:
        tree = ET.parse(fichero)
        root = tree.getroot()
    except:
        print("El fichero no existe")
    return root

def leerCampo(cadena="Introduce campo:"):
    valido = False
    while(not valido):
        campo = input(cadena)
        campo.strip()
        if(len(campo)>2):
            valido = True
        else:
            print("Error",end=" - ")
    return campo

def prettify(elem):
    from xml.etree import ElementTree
    from xml.dom import minidom
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='  ')

def mostrar(root):
    print(prettify(root))

def guardar(root):
    salida = prettify(root)
    file = open("ejer1_concesionario.xml","w")
    file.write(salida)
    file.close()


def ejer1():
    print("CREAR")
    root = leerXML("ejer1_concesionario.xml")
    if(root==None): #Si no hay un XML anterior creo el elemento raiz
        root = Element('Concesionario')

    salir = ""
    while(salir.lower()!='s' and salir.lower()!='si'):
        mat = leerCampo("Introduce matricula:")
        mar = leerCampo("Introduce marca:")
        mod = leerCampo("Introduce modelo:")
        col = leerCampo()
        coche = Element('Coche')
        matri = ET.SubElement(coche,'Matricula')
        matri.text = mat
        marca = ET.SubElement(coche,'Marca')
        marca.text = mar
        modelo = ET.SubElement(coche,'Modelo')
        modelo.text = mod
        color = ET.SubElement(coche,'Color')
        color.text = col
        root.append(coche)
        salir = input("Quieres terminar? si/no ")
    #Mostramos
    mostrar(root)
    #Guardamos
    guardar(root)
    
def buscar(root, mat):
    #print(len(root))
    encontrado=-1
    pos=0
    while(pos<len(root) and encontrado==-1):
        coche = root[pos]
        print("BUSCAR-coche",coche[0].text)
        if(coche[0].text==mat):
            encontrado = pos
        pos+=1
    return encontrado
    
def ejer2():
    print("BORRAR")
    root = leerXML("ejer1_concesionario.xml")
    if(root==None): #Si no hay un XML anterior creo el elemento raiz
        root = Element('Concesionario')
    
    salir = ""
    while(salir.lower()!='s' and salir.lower()!='si'):
        mat = leerCampo("Introduce matricula:")
        pos = buscar(root,mat)
        if(pos != -1):
            opcion = input("Estas seguro de querer borrar? s/n")
            if(opcion.lower()=="s" or opcion.lower()=="si"):
                #del(root[pos])
                root.remove(root[pos])# tambien lo haria
            else:
                print("Coche no borrado")
        else:
            print("Coche no encontrado")
            
        salir = input("Quieres terminar? si/no ")
    
    #Mostramos
    mostrar(root)
    #Guardamos
    guardar(root)   

print("Empezamos")

ejer1()

ejer2()

print("Fin")
