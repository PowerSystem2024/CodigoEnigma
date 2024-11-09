# Argumentos, Variables en funcionees
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: #Se va a convbertir en una tupla 
        print(nombre)
listarNombres("Lucas","Jose","Claudia","Rosa","Maria")
listarNombres("Marcos","Daniel","Romina","Marcela","Carlos")

def listarTerminos(**terminos): # Lo mas utilizado es  **kwargs para recibir los argumentos : key word argument
    for llave , valor in terminos.items():
        print(f"{llave}: {valor}")

listarTerminos() # No recibe nada , nada se va a mostrar 
listarTerminos(IDE = "Integrated Develoment Enviroment", PK = "Primaruy Key ")
listarTerminos(Nombre = " Lionel Messi ")



