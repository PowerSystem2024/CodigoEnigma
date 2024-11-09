# Desempaquetado de listas o list Unpacking
def show(name , lasName):
    print(name+" "+lasName)
    person = ["Agustin","Colombo"]
    show(person[0],person[1])# Pasamos uno por uno los datos de la lista a la funcion
    show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
    
    person2 =("Osvaldo ", "Giordanini") # desempaquetamos a traves de una tupla
    show(*person2)
    person3 = {"lastname": "Lucero,","Name ":"Natalia"}
    show(**person3)
    