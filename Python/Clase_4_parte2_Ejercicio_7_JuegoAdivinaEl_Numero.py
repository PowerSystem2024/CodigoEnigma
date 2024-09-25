#Ejercicio 7: Juego adivina el numero 
#Realizar un juego para adivinar un numero. para ello se debe 
#generar un numero aleatorio entre 1 - 100 , y luego ir pidiendo numeros 
# incicando " Es mayor " o "Es menor " segun sea mayor o menor 
# con respecto a N. El proceso termina cuando el usuario acierta y alli
# se debe mostrar el numero de intentos 

import random 
print("Juego Adivina el numero:")
aleatorio = random.randit(0,100) # toma del 0 al 100 literal , generamos un numero aletorio
contador = 0 
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("No es el numero , digite un numero menor")
    elif numero < aleatorio:
        print("No es el numero digite un numero mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el numero {aleatorio}")
        break # Rompe el ciclo y el bucle 
print(f"numero de intentos: {contador}")

