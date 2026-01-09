import sqlite3

def crearDB():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS CONTACTOS
                         (ID            INTEGER PRIMARY KEY AUTOINCREMENT,
                         NOMBRE         VARCHAR(25)     NOT NULL,
                         APELLIDOS      VARCHAR(25)     NOT NULL,
                         DIRECCION      CHAR(50),
                         TELEFONO       VARCHAR2(50),
                         EDAD            INT            NOT NULL);''')
    print("Table creada correctamente");
    conn.commit()
    cursor.close()
    return conn

def alta(conn):
    nom=input("Introduce nombre:")
    ape=input("Introduce apellidos:")
    direc=input("Introduce direccion:")
    tel=input("Introduce telefono:")
    edad=input("Introduce edad:")
    
    comando = "INSERT INTO CONTACTOS (NOMBRE,APELLIDOS,DIRECCION,TELEFONO,EDAD) \
                  VALUES ('"+nom+"','"+ape+"','"+direc+"','"+tel+"',"+edad+" )"
                  
    #print("INSERT:",comando)
    cursor = conn.cursor()
    cursor.execute(comando);
    conn.commit()
    cursor.close()
    
    print("Alta realizada con EXITO");

def mostrar(lista):
    print("\n\n------------")
    print("-- AGENDA --")
    print("------------\n")
    cursor = conn.execute("SELECT * from CONTACTOS")
    for row in cursor.fetchall():
        print( "ID = ", row[0])
        print( "NOMBRE = ", row[1])
        print( "APELLIDOS = ", row[2])
        print( "DIRECCION = ", row[3])
        print( "TELEFONO = ", row[4])
        print( "EDAD = ", row[5], "\n")

    print("------------\n")
                
        
def modificacion(conn):
    ape=input("Introduce apellidos del contacto a borrar:")
    cursor = conn.cursor()

    contactos = cursor.execute("SELECT * from CONTACTOS where apellidos="+ape+"")   
    contactos = contactos.fetchall()
    if(len(contactos)>0):
        for row in contactos:
            print( "ID = ", row[0])
            print( "NOMBRE = ", row[1])
            print( "APELLIDOS = ", row[2])
            print( "DIRECCION = ", row[3])
            print( "TELEFONO = ", row[4])
            print( "EDAD = ", row[5], "\n")
            
        tel=input("Introduce el nuevo telefono:")
        
        opcion = input("¿Estas seguro de querer modificar? s/n")
        if(opcion.upper()=="S"):
            conn.execute("UPDATE CONTACTOS set telefono = "+tel+" where apellidos = "+ape)
            print("Total number of rows updated :", conn.total_changes)
            conn.commit()        
                        
def baja(conn):
    
    ape=input("Introduce apellidos del contacto a borrar:")
    cursor = conn.cursor()

    contactos = cursor.execute("SELECT * from CONTACTOS where apellidos="+ape+"")    
    contactos = contactos.fetchall()
    if(len(contactos)>0):
        for row in contactos:
            print( "ID = ", row[0])
            print( "NOMBRE = ", row[1])
            print( "APELLIDOS = ", row[2])
            print( "DIRECCION = ", row[3])
            print( "TELEFONO = ", row[4])
            print( "EDAD = ", row[5], "\n")
        
        opcion = input("¿Estas seguro de querer borrar? s/n")
        if(opcion.upper()=="S"):
            cursor.execute("DELETE from CONTACTOS where ID = 2;")
            conn.commit()

        
def borrarBD():
        conn = sqlite3.connect('test1.db')
        print("Opened database successfully")
        cursor = conn.cursor()

        valor = cursor.execute("DROP TABLE CONTACTOS;")
        conn.commit()
        cursor.close()
        print("tables deleted")
        conn.close()
        
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

print("Empezamos")
conn = crearDB()
opcion =""
while(opcion!='0'):
    opcion=menu()
    if(opcion=='1'):
        alta(conn)
    elif(opcion=='2'):
        baja(conn)
    elif(opcion=='3'):
        modificacion(conn)
    elif(opcion=='4'):
        buscar(conn)
    elif(opcion=='5'):
        mostrar(conn)
    elif(opcion=='0'):
        print("Terminamos")
    else:
        print("Opcion no valida")
        
conn.close()

print("Fin")

