def fun1(a,b=2):
    print(a,b)
    
   
def fun2(fijo,*variable):
    print(fijo)
    print(variable,type(variable))
    for i in variable:
        print(i)
        
def fun3(fijo,*variable,**pares):
    print(fijo)
    for i in variable:
        print(i)
    print(pares,type(pares))
    for i in pares:
        print(pares[i])
        
def suma(a,b):
    print("Suma",a+b)

print("Empezamos")

fun1(5)
fun1(7,6)

a = fun1
a(55)

fun1(b='cadena1',a='cadena2')

fun2("fijo","v1","v2")
fun2("fijo2","v1","v2",'v3','v4')

fun3("fijo2","v1","v2",cad1='abc',cad2=12345)

operandos=[5,7]
suma(*operandos)

ope={'a':4,'b':2}
suma(**ope)

print("Fin")
