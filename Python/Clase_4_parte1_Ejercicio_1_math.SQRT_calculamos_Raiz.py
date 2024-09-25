import math #Importamos la clase math para hacer uso de la funcion sqrt
#Ejercicio de Matematicas: 
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo:"))
while numero < 0:
    print("Error -> Deberia ser un numero positivo ")
    numero = int(input("Digite un numero positivo: "))
print(f"Su raiz cuadrada es: {math.sqrt(numero):.2f} ")
