#Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
#numericos, utilizando argumentos variables *args como parametro de la 
#Funcion y agregar como resultado la suma de todos los valores pasados 
# como argumentos:

def sumarValor(*args): #Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

#llamamos a la funcion 
print(sumarValor(3,5,9,2,1))

    