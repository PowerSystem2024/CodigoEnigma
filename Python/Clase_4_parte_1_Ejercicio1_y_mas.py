#Ejercicio 1 : Eliminar duplicados de una lista 
# escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos , por ultimo mostrar la lista 

# creamos una lista 
lista = [1, 2, 3, "Ariel", 7.7, 3, "Alberto", 5, "Ariel", 2, "Albero"]
#conjunto = set(lista)  # convertimos la lista a un conjunto de tipo set
#lista = list(conjunto)  # convertimos el conjunto a una lista
lista = list(set(lista)) # es lo mismo que lo de arriba solo que esta en una linea
print(lista)
