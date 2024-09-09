# Repaso de set o conjunto
# para definir un conjunto 
conjunto2 = set()
conjunto1 = {"bye"} #si esta asi no va a funcionar hay que agregarle algo para que de inicialice , con las llaves solas no se puede comenzar un conjunto
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el numero 3 NO esta en el conjunto1 ( y nos devuelve un valor booleano True o False  )
# como hacer una igualdad de dos conjuntos 
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# operaciones en conjuntos 
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos # si hay una igualdad de conjuntos se borra uno y imprime solo uno
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # que elemento tienen en comun 
print(conjunto3)
conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta em el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o son diferentes emtre ambos conjuntos
print(conjunto3) 

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # A qui preguntamos si un conjunto es subconjunto dentro de otro responde con un valor booleano
print(conjunto2.issubset(conjunto1))
print(conjunto3.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))


print(conjunto3.issubset(conjunto1)) # preguntamos si los elementos del conjunto 1 estan en el 3
print(conjunto3.issubset(conjunto2)) # si es verdadero quiere decir que el conjunto 3 es un super conjunto porque el conjunto 1 y 2 estan dentro del 3 
print(conjunto2.issubset(conjunto3)) 
 
# como saber si ambos conjuntos son disconexos osea que no compoarten ningun elemento en comun
print(conjunto1.isdisjoint(conjunto2))  # no hay cosas en comun

# convertir un conjunto totalmente inmutable 
conjunto1 = frozenset # esto hace que el conjunto sea totalmente inmutable
# No se puede agregar , modificar ni eliminar elementos del conjunto

# repasos de diccionarios
diccionarioNuevo = {"Azul" : "Blue", "Rojo": "Red", "Amarillo": "Yellow","Verde": "Green"}
print(diccionarioNuevo)
# Como eliminar
del(diccionarioNuevo["Azul"])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferernte tipos de datos
diccionario2 = {"Ariel":{"Edad": 40, "Altura": 1.83}, "Osvaldo": [45,1.85], "Natalia":[35,1.67]}
print(diccionario2)
# Tarea echa Agregar como minimo 4 jugadores mas con todos sus datos
seleccionArgentina = {
    10 : {"Nombre": "Lionel Messi", "Edad": 35, "Altura" : 1.70, "Precio": "50 Millones", "Posicion": "extremo derecho"},
    11 : {"Nombre": "Angel Di Maria", "Edad": 34, "Altura" : 1.80, "Precio": "12 Millones", "Posicion": "extremo derecho"},
    24 : {"Nombre": "Paulo Dybala", "Edad": 28, "Altura" : 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19 : {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura" : 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa central"},
    1 : {"Nombre": " Franco Armani", "Edad": 35, "Altura" : 1.89, "Precio": "3.5 Millones", "Posicion": "portero"},
    9 : {"Nombre": "Julian ALvarez", "Edad": 24, "Altura" : 1.70, "Precio": "90 Millones", "Posicion": "Delantero"},
    22 : {"Nombre": "Lautaro Martinez", "Edad": 27, "Altura" : 1.74, "Precio": "110 Millones", "Posicion": "Delantero"},
    20 : {"Nombre": "Alexis MacAlister", "Edad": 25, "Altura" : 1.76, "Precio": "40 Millones", "Posicion": "mediocampista izquierdo"},
    3 : {"Nombre": "Nicolas Tagliafico", "Edad": 32, "Altura" : 1.70, "Precio": "8 Millones", "Posicion": "defensor izquierdo"},
}
print(seleccionArgentina())
for llave in seleccionArgentina.items():
    print( llave, valor)
print( "Tenemos cargados en el diccionario la cantidad de jugadores: ", end = "")
print(len(seleccionArgentina))

# Metodos PILAS: se usa en las listas
pila = [1,2,3] # esto es una lista

# Agregar elementos a la pila por el final
# siempre agregar o sacar con los ultimos elementos
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # elimina el ultimo numero de la lista y lo guarda en la variable
print(f"Sacamos el elemento: {elementoBorrado}")
print(f"La pila ahora quedo asi: {pila}")
 
#Metodos con listas lamado COLA 
# estructura de datos de tipo fifo(first input / first output) //banco , una cola y van atendiendo al que primero llega
cola = ["Ariel","Osvaldo","Liliana","Pilar"]

#Agregamos elementos al final de la cola
cola.append("Natalia")
cola.append("Jose")
print(cola)
 
# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido el cliente{seRetira}") # Atiende a Ariel
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente{seRetira}") # Atiende a Osvaldo
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente{seRetira}")# Atiende a Liliana
print(cola)


