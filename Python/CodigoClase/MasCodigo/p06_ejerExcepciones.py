print("Empezamos")


incorrecto = True
while incorrecto:
    try:
        num1=int(input("Introduce num1:"))
        incorrecto = False
    except:
        print("Opcion incorrecta vuelva a intentarlo")
        
incorrecto = True
while incorrecto:
    try:
        num2=int(input("Introduce num2:"))
        incorrecto = False
    except:
        print("Opcion incorrecta vuelva a intentarlo")

print("La suma es:",num1+num2)

print("Fin")
