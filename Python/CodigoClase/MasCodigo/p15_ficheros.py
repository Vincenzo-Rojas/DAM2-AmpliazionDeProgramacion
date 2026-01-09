def ejem1_escritura():
    file1 = open("myfile.txt", "w")#file1 = open("myfile.txt", "a")Para anyadir contenido y no borrar lo anterior
    L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

    # \n is placed to indicate EOL (End of Line)
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes
    
    
def ejem2_lectura01():
    fich = open("myfile.txt","r")
    contenido = fich.read()
    print(contenido,type(contenido))
    fich.close()

def ejem2_lectura02():
    fich = open("myfile.txt","r")
    contenido = fich.readlines()
    print(contenido,type(contenido))
    print("***********")
    for linea in contenido:
        print(linea)
    fich.close()
    
def ejem2_lectura03():
    fich = open("myfile.txt","r")
    linea = fich.readline()
    while(linea):
        print(linea,end="")
        linea = fich.readline()    
    fich.close()

print("Empezamos")
#ejem1()
ejem2_lectura03()
print("Fin")
