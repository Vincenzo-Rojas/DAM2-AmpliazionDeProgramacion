def fun1():
    print("Funcion 1")

def fun2():
    return 1,2,"cadena"

print("Empezamos")
print(fun1())

a = fun2()
print(a,type(a))

a,b,c = fun2()
print(a,b,c)

dic = {1:"a",2:"b"}
print(dic)
print("------")
for i,j in dic.items():
    print(i,j)

print("Fin")
