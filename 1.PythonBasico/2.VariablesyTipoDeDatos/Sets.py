"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
September 25, 2017
"Conjuntos"
"""
# Creacion de conjunto
x = set([1,2,3,4]) # A partir de una lista
print(x)

y = set((1,2,3,4,4)) # A partir de una tupla
print(y)

# Creacion de conjunto

w={1,2,3,4,"Daniel"}

"Daniel" in w

"Carlos" not in w



# Operaciones con conjuntos

# Agrega elementos
x = set([1,2,3,4])
x.add(5)
x.add(5) # un conjunto no almacena elementos repetidos
print(x)

# Eliminar elementos
x = set([1,2,3,4])
x.remove(4)
x.discard(3)
print(x)

# Union
x = set([1,2,3,4])
y = set([3,4,5,6])
z = x | y 
print(z)

# Interseccion 
x = set([1,2,3,4])
y = set([3,4,5,6])
z = x & y
print(z)

# Diferencia
x = set([1,2,3,4])
y = set([3,4,5,6])
z = x - y 
print(z)

#Convertir una lista a un conjunto y luego a una lista

l=[1,2,3,3,4,4,4,5,6,6,6]
l=list(set(l))
print(l)


