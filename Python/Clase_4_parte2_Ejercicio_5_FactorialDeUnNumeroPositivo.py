# Ejercicio: 9 Factorial de un nmero positivo
#Hacer un progrma para calcular el factorial de un numero positivo
numero = int(input("Digite un numero: "))
while numero < 0: # Mientras el numero sea negativo 
    print("Error -> el numero tiene que ser positivo")
    numero = int(input("Digite un numero: "))
factorial = 1 # la variable para calcular rl factorial
for i in range (1,numero+1):
    factorial *= i
print(f" El factorial del numero {numero} positivo ingresado es : {factorial}")
