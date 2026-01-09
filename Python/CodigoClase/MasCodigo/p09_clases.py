
class Clase1():
    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary
        
    def __str__(self):
        return self.name+" - "+str(self.salary)
        
class Clase2():
    def __init__(self):
        self.at1 = 1
        self.at2 = 'valor'

class Empleado():
    empCount=0
    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary
        Empleado.empCount += 1
    
    def displayCount(self):
        print("Contador de empleados:",Empleado.empCount)
        print(f"Contador de empleados: {Empleado.empCount}")
        print("Contador de empleados: %d" % Empleado.empCount)
        
    def mostrarEmpleado(self):
        print("Empleado:",self.name," - ",self.salary)
        
    def __del__(self):
        nombreClase = self.__class__.__name__
        print(nombreClase, "borrado")
                
    def __str__(self):
        return "Empleado:"+self.name+" - "+str(self.salary)
        

print("Empezamos")
c1 = Clase1()
c2 = Clase1("Juan")
c3 = Clase1("Jose",1000)
print(c1)
print(c2)
print(c3)

e1 = Empleado()
e2 = Empleado("Juan")
e3 = Empleado("Jose",1000)
print(e1)
print(e2)
print(e3)
e1.displayCount()
#Empleado.displayCount()
e1.mostrarEmpleado()

del(c2)
#print(c2)

print("Fin")
