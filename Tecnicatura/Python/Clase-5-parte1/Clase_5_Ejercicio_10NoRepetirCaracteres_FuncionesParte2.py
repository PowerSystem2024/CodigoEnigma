# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadenapor teclado, luego
# meter los caracteres en una lista sin repetir caracteres 
 
cadena = input("Digite una cadena: ")
lista = []
for i in cadena:
    if i not in lista:# Si el caracter aun no esta en la lista 
        lista.append(i) #Lo agrgamos a la lista 
print(f"Lista de caracteres sin repetir ninguno: {lista}")
 