#tipo set
planetas = {"Marte","Jupiter","Venus"}
print(len(planetas)) # usamos la funcion eln que nos dice el largo osea la cantidad que hay en este caso hay 3

# Revisar si un elemento existe dentro de set 
print("Marte" in planetas) #nos va a poner es que true si tiene un error va a dar un false

# Agregar un elemento
planetas.add("Tierra") # add es una funcion , agregamos un elemento al set 
print(planetas) # no se pueden agregar elementos duplicados 

# Eliminar elementos 
planetas.remove("Jupiter") # esta funcion ante un mal ingreso u existencia del elemento nos da error
print(planetas)
# existe otra forma donde no tira un error cuando lo esta exactamente igaul ejemplo si nos falta una mayuscula
# es .discard 
planetas.discard("tierra") # esta funcion no nos presenta ningun error si lo ingresamos mal , no lo borrara
print(planetas) # si esta mal escrito no nos va a borrar mada del programa y no nos va a generar ningun error
 # Limpiar set 
planetas.clear()
print(planetas)
#eliminar set o conjunto
del planetas 
#print(planetas) # nos da un error porque eliminamos el conjunto

# "Maradona" : 10 un diccionario esta compuesdto por dos elementos 
# una llave y un valor 
# dict(key,value)
diccionario = {
    "IDE" : "Integrated Development Enviroment",
    "POO" : "Programacion Orientada a Objetos",
    "SABD" : "Sistema de Administracion de Base de Datos "
}
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

# OTRA FORMA DE RECUPERAR UN ELEMENTO 
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# Modificamos elementos 
diccionario["IDE"] = "Entorno de desarrollo integrado "
print(diccionario)

# como recorrer elementos 
for termino in diccionario:
    print(termino)

for termino,  valor in diccionario:# Recorremos mostrando solo las llaves 
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario 
for termino in diccionario.keys(): # estamos usanod una funcion 
    print(termino) # Muestra solo las llaves 

for valor in diccionario.values(): # usamos una funcion para acceder el valor 
    print(valor)  #Funciones para recorrer y acceder al diccionario

# comprobar la existencia de algun elemento
print( "IDE" in diccionario) # Devuelve un valor booleano (true) o (false)

# Agregar un elemento al diccionario
diccionario["PK"] = "Primary key"
print(diccionario)

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Como vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro 

# Concatenamos listas 
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2
print(lista3)
# funcion para agregar varios elementos a una lista 
lista3.extend([7,8,9])
print(lista3)
#funcion para ubicar en que indice esta el valor ingresado
print(lista3.index(5)) # Nos dice en que indice esta arranca desde el (0)
# print(lista3.index(0)) esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repeidos hay dentro de una lista 
print(lista3.count(1))# cuenta cuantos valores iguales hay dentro de la lista en este caso no hay tendria que ponerlos

# para poner al reves una lista 
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitendo sus elementos 
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento 
lista3.sorta() # ORDENA LOS NUMEROS ASENDENTEMENTE 1,2,3,4,5,6,7,8,9 ETC
print(lista3)
lista3.sort(reverse=True) #Ordena descendentemente osea 9,8,7,6,5,4,3,2,1, etc 
print(lista3)

#Repaso de tuplas
tupla = (4, "Hola", 6,78,[1,2,78],4,"Hola") # puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # accion booleana , su respuesta es un tipo de booleana 
# lo que podemos usar dentro de tuplas son: index , count, len 
# en tuplas se puede convertir de tupla a lista y de lista a tupla 