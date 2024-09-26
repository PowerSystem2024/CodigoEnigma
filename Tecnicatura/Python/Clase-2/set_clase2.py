planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas))

print("Jupiter" in planetas)

planetas.add("Tierra")  # Agregar un elemento
print(planetas)

planetas.remove("Jupiter") # Eliminar un elemento
print(planetas)
planetas.discard("Tierra")

planetas.clear()
print(planetas)

del planetas
print(planetas)  # Error al haber eliminado el conjunto