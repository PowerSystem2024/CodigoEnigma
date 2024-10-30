# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo númerico, utilizando argumentos variables  *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumento

def multiplicar_valores(*args): # Cantidad de parámetros indefinidos
    resultado = 1 # El cero no ayuda a multiplicar
    for valor in args:
        resultado *= valor
    return resultado

print(multiplicar_valores(3, 5, 15))