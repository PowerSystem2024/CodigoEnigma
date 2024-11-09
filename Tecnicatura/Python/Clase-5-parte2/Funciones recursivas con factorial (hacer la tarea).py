#Clase N°5 parte 1  
# Argumentos, Variables en funcionees
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: #Se va a convbertir en una tupla 
        print(nombre)
listarNombres("Lucas","Jose","Claudia","Rosa","Maria")
listarNombres("Marcos","Daniel","Romina","Marcela","Carlos")
#Clase N°5 parte 2 
def listarTerminos(**terminos): # Lo mas utilizado es  **kwargs para recibir los argumentos : key word argument
    for llave , valor in terminos.items():
        print(f"{llave}: {valor}")

listarTerminos() # No recibe nada , nada se va a mostrar 
listarTerminos(IDE = "Integrated Develoment Enviroment", PK = "Primaruy Key ")
listarTerminos(Nombre = " Lionel Messi ")
# Sigue la clase 5 parte 2 pero en otro video 

def desplegarNombres(nombres):
    for nombres in nombres:
        print(nombres)
nombres2 = ["Tito" , "Pedro ", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
#desplegarNombres(10,11) # No es un objeto iteralble 
desplegarNombres((10,11)) #Corresponde a una tupla osea la convertimos a un a tupla , en un solo elemento no oloviudar la coma ya que no es una tupla si no esta 
desplegarNombres((22,55)) #La convertimos en una lista 

#Clase 5 parte 2 

#Funciones Recursivas 
def factorial(numero):
    if numero == 1: #Caso Base 
        return 1
    else:
        return numero * factorial(numero-1)#Caso Recursivo 
resultado = factorial(5) # Lo hacemos en codigo duro 
print(f"El factorial del numero 5 es: {resultado}")



