import sqlite3

def ejem1():
	conn = sqlite3.connect('test1.db')
	print("Opened database successfully");
	

	conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
			 (ID INT PRIMARY KEY     NOT NULL,
			 NAME           TEXT    NOT NULL,
			 AGE            INT     NOT NULL,
			 ADDRESS        CHAR(50),
			 SALARY         REAL);''')
	print("Table created successfully");
	
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS COMPANY2
			 (ID INT PRIMARY KEY     NOT NULL,
			 NAME           TEXT    NOT NULL,
			 AGE            INT     NOT NULL,
			 ADDRESS        CHAR(50),
			 SALARY         REAL);''')
	print("Table created successfully");
	#datos = cursor("show tables")
	cursor.close()
	conn.close()

def ejem2():
	conn = sqlite3.connect('test1.db')
	print("Opened database successfully");
	
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (1, 'Paul', 32, 'California', 20000.00 )");

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

	conn.commit()
	print("Records created successfully");
	conn.close()
	
def ejem3():
	conn = sqlite3.connect('test1.db')
	print("Opened database successfully")

	cursor = conn.execute("SELECT id, name, address, salary from COMPANY")	
	print("CURSOS",type(cursor))
	for row in cursor:
	   print("ROW",type(row))
	   print("ID = ", row[0])
	   print("NAME = ", row[1])
	   print("ADDRESS = ", row[2])
	   print("SALARY = ", row[3], "\n")

	print("Operation done successfully")
	conn.close()
	
def ejem4():
	conn = sqlite3.connect('test1.db')
	print("Opened database successfully")

	conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
	print("Total number of rows updated :", conn.total_changes)
	conn.commit()
	print("Total number of rows updated :", conn.total_changes)

	cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
	for row in cursor:
	   print( "ID = ", row[0])
	   print( "NAME = ", row[1])
	   print( "ADDRESS = ", row[2])
	   print( "SALARY = ", row[3], "\n")

	print("Operation done successfully")
	conn.close()

def ejem5():
	conn = sqlite3.connect('test1.db')
	print("Opened database successfully")

	conn.execute("DELETE from COMPANY where ID = 2;")
	conn.commit()
	print("Total number of rows deleted :", conn.total_changes)

	cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
	for row in cursor:
	   print( "ID = ", row[0])
	   print( "NAME = ", row[1])
	   print( "ADDRESS = ", row[2])
	   print( "SALARY = ", row[3], "\n")

	print("Operation done successfully")
	conn.close()
	
def ejem6():
	conn = sqlite3.connect('test1.db')
	print("Opened database successfully")
	cursor = conn.cursor()

	valor = cursor.execute("DROP TABLE COMPANY;")
	valor = cursor.execute("DROP TABLE COMPANY2;")
	conn.commit()
	cursor.close()
	print("tables deleted")
	conn.close()

print("Empezamos")
ejem1()
print("***")
ejem2()
print("***")
ejem3()
print("***")
ejem4()
print("***")
ejem5()
print("***")
ejem6()
print("Fin")
