import math # Incorporamos la clase math para usar la función de raiz cuadrada
# Clase 4:

# Ejercicio de Colecciones 1

# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

lista = [2, True, 'Hola', 13, 13, 17, 23, 23, 'Hola']
print(lista)
conjunto = set(lista) # convertimos a conjunto
print(conjunto)

lista = list(conjunto) # convertimos a lista
print(lista)

# Otra opción en una linea
lista = list(set(lista))

# Ejercicio de Colecciones 2

# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

# Eliminar elementos repetidos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = conjunto1 | conjunto2
solo1 = list(conjunto1 - conjunto2) # Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # Solo muestra el conjunto2
interseccion = list(conjunto & conjunto2) # Mostramos ambas listas

print(f'Lista de palabras que aparecen en las listas: {union}')
print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}')
print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}')
print(f'Lista de palabras que aparecen en ambas listas: {interseccion}')

# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []
p ={'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(p)
p ={'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p)
p ={'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(p)

print(personajes)

# Ejercicio 1 con Matemáticas y la clase path
# Sacar la raiz cuadrada de un número positivo

numero = int(input('Ingrese un número positivo'))

while numero < 0:
    print('Error, debería ser un número positivo')
    numero = int(input('Ingrese un número positivo'))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}') # Deja solo dos digitos de decimal



