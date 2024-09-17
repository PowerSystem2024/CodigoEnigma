#lista = Ariel , liliana , natalia , osvaldo 
# Colecciones en Python

# Las listas es lo que se cooce en otros lenguajes como arrgelos o vectores 
nombres = ["Naty", "Osvaldo" , "Lily" ,"Ariel"]
print(nombres) 
print(nombres[0]) #me imprime solo el elemento 0 de la lista osea (Naty) 
print(nombres[1]) #me imprime solo el elemento 1 de la lista osea (osvaldo)
print(nombres[3]) #me imprime solo el elemento 3 de la lista osea (ariel)
print(nombres[-1]) #me imprime solo el elemento -1 de la lista osea (ariel)
print(nombres[-2]) #me imprime solo el elemento -2 de la lista osea (lily)
#---------------------------------------------------------------------------
nombres = ["Naty", "Osvaldo" , "Lily" ,"Ariel"]
print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0 ,1 pero no el indice 2
#ir al inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #indices a mostrar 0,1,2
# Desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos un valor  
nombres[2] = "liliana" 
nombres[0]
print(nombres)
#iterar una lista
for nombres in nombres: #nombre es singular , a lista es plural 
    print(nombres)
else: print("Se acabaron los elementos de la lista") 
#----------------------------------------------------------------------------
# nos dice la cantidad de elementos que tiene una lista usamos la de (nombres)
# preguntamos cuantos elementos tiene 
print(len(nombres)) # le pasamos como parametro la lista 
# resultado es 4 , ya que son 4 nombres dentro de la lista 
# Agregamos un elemento a la lista en el final de la lista con la funcion .append 
# UNA LISTA PUEDE TENER DISTINTOS TIPOS DE DATOS PUEDE HABER TIPO BOOLEANO , FLOTANTE , NOMBRE Y NUMEROS ENTEROS
nombres.append("Marcelo") 
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres) # se ingresa en el final de la lista 
# ahora insertamos pero en un lugar especifico de la lista con la funcion .insert Ejemplo: 
nombres.insert(1, "Alberto") # necesitamos un entero y uno de tipo string que en este caso es el nombre alberto
print(nombres)
# Otro ejemplo:
nombres.insert(3, "Debora")
print(nombres)
#Para eliminar un elemento de la lista usamos la funcion remove
nombres.remove("Alberto")
print(nombres)
#Eliminar el ultimo elemento ingresado , no el ultimo de la fila en este caso el ultimo elemento ingresado es debora
# usamos la funcion .pop
nombres.pop()
print(nombres)
#Eliminar un indice especifico con la funcion del
#del nombre[2] # del es delete 
#print(nombres)
#Eliminar o borrar o limpiar todos los elementos 
nombres.clear()
print(nombres)
#eliminar la lista 
del nombres
print(nombres)

#*******#
#Tuplas:
#*******#
#Las tuplas no se pueden eliminar , son inmutables , no modificable esta es la gran diferencia entre 
# tuplas y listas  
# para que sea tu`pla se define como ("manzana",)`la coma los parentesis y las comillas van para que sea una dupla
# Definimos una tupla , no se usan los [] se usan ()
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))
# acceder a un elemento, para esto corchetes no parentesis 
print(cocina[0])
# mostrar de manera inversa 
print(cocina[-1]) # como lo vimos en las listas
#acceder a un rango 
print(cocina[0:1]) # el 1 , nos va a imprimir uno solo osea en este caso cuchara , para que muestre cuchillo que esta en la 
                   # en la posicion 2 hay que poner [0:2]
# Ejemplo:
verduras = ("papa",) #Una tupla necesita aunque sea de un elemento: la coma de lo contrario solo seria un tipo string cadena

# Recorremos los elementos de la tupla
for cocina in cocina: # print esta usando /n para saltos de linea / tendria que estar al reves pero no me deja darla vuelta
    print(cocina , end= " ") #usamos end= para eliminar los saltos de lineas 

# no se puede hacer una modificacion en la dupla ejemplo
cocina[0] = "plato"
print(cocina) # Con esto va a salir un error 
# la unica foma de modificar una tupla es pasar la tupla a lista , modificamos y luego pasamos de lista a tupla
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)        # Esto es una mala practica pero lo dejo por las dudas
print("/n ", cocina )

#Eliminar una dupla:
del cocina 
print(cocina)