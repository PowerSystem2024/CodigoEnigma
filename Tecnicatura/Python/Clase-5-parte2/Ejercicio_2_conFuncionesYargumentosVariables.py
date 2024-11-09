#Ejercicio 2 : Funcion con * args para multiplicar
# Crear una funcion para multiplicar los valores recibidos 
# de tipo numerico , utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumento


# Definimos la funcion para multiplicar 
def multiplicar_valores(*numeros): #El mas utilizado es *args
    resultado = 1 # El cero no nos ayuda a multiplicar 
    for numero in numero:
        resultado *= numero
    return resultado 

# Llamamos la funcion 
print(multiplicar_valores(3,5,15,3)) # le pasamos los argumentos 

