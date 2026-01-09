import redis

print("Empezamos")

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


#Anyadir
r.set('clave1', 'valor1')
# True
print(r.get('clave1'))
# bar
r.set('con_1', '1;1;1;1;1')
r.set('con_2', '2;2;2;2;2')
r.set('con_3', '3;3;3;3;3')
r.set('con_4', '4;4;4;4;4')

print("**************")
#Mostrar todos
all_keys = r.keys('*')
print(all_keys)
for i in all_keys:
    print(r.get(i))

print("**************")
#Mostrar todos
all_keys = r.keys('con*')
print(all_keys)
for i in all_keys:
    print(r.get(i))

print("**************")
print("Borramos",r.delete('con_2'))
print("Modificamos:",r.set('con_3', '33;33;33;33;33'))
print("**************")
#Mostrar todos
all_keys = r.keys('*')
print(all_keys)
for i in all_keys:
    print(r.get(i))
    


print("**************")    
print("Limpiamos")
for i in all_keys:
    print("Borramos:",i)
    r.delete(i)
print("**************")

print("Fin")
