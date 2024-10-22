# Clase 1:
# Ejercicio 1
# Iteran un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo de ejecución: 0,3,6,9

# Ejercicio 2
# Crear un rango de 2 a 6 e imprimirlos
# Ejemplo de ejecución: 2,3,4,5,6

# Ejercicio 3
# Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9

#Sintaxis range (inicio<opcional>, fin <requerido>, incremento <opcional>)

print('Ejercicio 1: Rango de 0 a 10 con números divisibles entre 3')

for i in range(11):
    if i % 3 == 0:
        print(i)

print('Ejercicio 2: Rango de 2 a 6')

rango = range(2,7)
for i in rango:
    print(i)

print('Ejercicio 3: Rango de 3 a 10, de 2 en 2')

rango2 = range(3,11)
for i in range(3,11,2):
    print(i)

# Ejercicio Tupla:
# Dada la siguiente tupla, crear una lista que solo incluya los números menores a 5
# e imprima por consola [1,3,2]
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)

