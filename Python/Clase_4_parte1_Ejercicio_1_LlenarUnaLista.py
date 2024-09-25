#Ejercicio 5: Llenar una listra
#llenar una lista con los numeros del 1 al 50 , luego mostrar la lista con el bucle for
#los elementos deben mostrarse se la siguiente forma #1-2-3-4-5-.....-50

lista = []
i = 1 
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i,end="-")

#Algoritmo eficas que lo hacemo en 1 linea y no en 5 
# lista = list(range(1,51))
# for i in lista:
#    print(i,end="-") 
