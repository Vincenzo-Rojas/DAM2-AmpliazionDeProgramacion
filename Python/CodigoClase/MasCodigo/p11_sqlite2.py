import sqlite3

def crearDB():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE if not exists Contactos
             (ID INT PRIMARY KEY     NOT NULL,
             nombre   varchar2(50)    NOT NULL,
             telefono   varchar2(15)     NOT NULL)''')
             
    print("Table created successfully")
    conn.close()

def insertar():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully");
    
    cont = contar()
    print("REgistros:",cont)
    nombre = "Pedro"
    telef = "77666"
    
    comando = "INSERT INTO Contactos (ID,nombre,telefono) \
          VALUES ("+str(cont)+", '"+nombre+"', \""+telef+"\" )"
    print(comando)
    #conn.execute(comando);
    
    fin = False
    while(not fin):
        cont +=1
        nombre = input("Introduce nombre:")
        telef = input("Introduce telefono:")
        opcion = input("Estas seguro de querer insertar?s/n ")
        if(opcion.lower()=="s"):
            comando = "INSERT INTO Contactos (ID,nombre,telefono) \
            VALUES ("+str(cont)+", '"+nombre+"', \""+telef+"\" )"
            print(comando)
            conn.execute(comando);
        opcion = input("Quieres insertar otro?s/n ")
        if(opcion.lower()=="n"):
            fin=True

    conn.commit()
    conn.close()
    
def mostrar():
    conn = sqlite3.connect('test2.db')
    cursor = conn.execute("SELECT * from Contactos")    
    for row in cursor:
       print("ID = ", row[0])
       print("NOMBRE = ", row[1])
       print("TELEFONO = ", row[2], "\n")


    print("Operation done successfully")
    conn.close()

def contar():
    conn = sqlite3.connect('test2.db')
    cursor = conn.execute("SELECT * from Contactos")    
    num = len(cursor.fetchall()) 
    conn.close()
    return num 
    

print("Empezamos")
crearDB()

insertar()
mostrar()

print("Fin")
