#Ejercicio: Uso de Rangos, antes de ver el video con la solución, debes intentar solucionarlo
#Ejercicio Nº1 iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3 
#Ejemplo de ejecucion: 3,5,6,9
print("Rango de 0 a 10 con numeros divisbles entre 3 ")
for i in range(11):
   if i % 3 == 0:
     print(i)
#Ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos 
# Ejemplo de ejecucion: 2,3,4,5,6
print("Rango con valores de inicio = 2 y fin = 6")
rango = range(2, 7)
for i in rango:
   print(i)
#Ejercicio Nº3: Crtear un rango de 3 a 10 pero con incremento de 2 en 2 , en lugar de 1 en 1
# Ejemplo de la ejecucion 3,5,7,9
print("rango de 3 a 10 con incremento de 2 en 2  ")
for i in range(3, 11, 2):
     print(i)

# EJERCICIO DE TUPLAS
# dada la siguiente tupla 
#tupla = (13,1,8,3,2,5,8) # definimos tupla
# crear una lista que soo incluya los numeros menores a 5 e imprima por consola [1,3,2]
tupla = (13,1,8,3,2,5,8)
lista = []  #definimos fla lista
#Filtramos los elementos menores a 5 de la tupla 
for elemento in tupla:
    if elemento < 5:
       lista.append(elemento)
print(lista)