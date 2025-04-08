# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#  suma de número pares del 2 al 30
#  suma = 240

a = int(input('Ingrese de dónde va a comenzar la suma: '))
b = int(input('Ingrese hasta dónde va a llegar la suma: '))
suma = 0
for i in range(a, b+1):
    if i%2==0:
        suma += i
print(f'\nLa suma de números pares dentro del rango es: {suma}')
