class Pajaro():
    nombre=""
    tipo=""
    
class Clase1():
    at1=""
    at2=0
    at3=Pajaro()
    
class Clase3():
    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary
        
    def __str__(self):
        return self.name+", "+str(self.salary)

class Clase4():
    def __init__(self):
        self.at1 = 1
        self.at2 = 'valor'
        
    def __str__(self):
        return str(self.at1)+", "+self.at2
        
class Empleado():
    contEmpleados = 0
    
    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary
        Empleado.contEmpleados +=1
        
    def __str__(self):
        return self.name+", "+str(self.salary)
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"limpiado")

print("Empezamos")

var1 = Clase3()
var2 = Clase3("Juan")
var3 = Clase3("Ana",500)
print(var1)
print(var2)
print(var3)
var4 =  Clase4()
print(var4)

em1 = Empleado()
print(em1)
em1 = Empleado("Juan",1500)
print(em1)
print(Empleado.contEmpleados)

print("*"*25)

o1 = Clase1()
print(o1)
print(o1.at2)
o2 = Clase1()
o2.at2 = 5
print(o2.at2)
o1.telefono = "666000333"
print(o1.telefono)
#print(o2.telefono)
del(o1.telefono)
#print(o1.telefono)


print("Fin")
