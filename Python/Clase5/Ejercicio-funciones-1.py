# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# númericos, utilizando argumentos variables *args como parámetro de la
# Función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

def sumar_valor(*args): # Cantidad de parámetros indefinidos
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3, 5, 9))

