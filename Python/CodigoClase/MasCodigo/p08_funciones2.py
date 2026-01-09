def suma(a,b):
	print(a+b)


def fun1(a,b,c=2,d=5):
	print(a,b,c,d)


def fun2(fijo,*variable):
	print(fijo)
	print(type(variable))
	for i in variable:
		print(i)
		
def fun2_2(*variable):
	suma=0
	for i in variable:
		suma+=i
	print(suma)
	
def fun3(fijo,*variable,**pares):
	print(fijo)
	print("----")
	for i in variable:
		print(i)
	print("----")
	for i in pares:
		print(pares[i])

def suma(a,b):
	print(a+b)
	
class Ejemplo():
	atrib1=""
	

print("Empezamos")

ej1= Ejemplo()
ej1.atrib1=55
print(ej1.atrib1)
Ejemplo.atrib1 = 1
print(Ejemplo.atrib1,"clase")
print(ej1.atrib1,"Objeto")

ej1.atrib2=77
print(ej1.atrib2)

ope={'a':4,'b':2}
suma(**ope)

print("+++++++++")

operandos=[5,7]
suma(*operandos)

suma(1,2)


print("+++++++++")

fun3("fijo2","v1","v2",cad1='abc',cad2=12345)

print("*"*25)

fun1(5,7)

fun1(b=1,a=2,d=3,c=4)

print("*"*25)

fun2("Fijo",1)
print("-"*25)
fun2("Fijo",1,2)
print("-"*25)
fun2("Fijo",1,2,5,6,7,8,9)

print("*"*25)

ope={'a':4,'b':2}
suma(**ope)

print("Fin")
