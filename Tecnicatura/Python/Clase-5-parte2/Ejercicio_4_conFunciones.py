#Ejercicio 4 : Calculadora de Inpuestos
#Crear una funcion para calcular el total de un pago incluyendo
#un inpuesto aplicado. (IVA)
#Formula: pago_total = pago sin inpuesto + pago_sin_impuesto *(inpuesto/100)
#Proporcione el pago sin inpuesto: 100
#Proporcione el monto del inpuesto:21%
#Pago con inpuesto: xxxxx

#Creamos la funcion que calcula el total del pago incluyendo el inpuesto 
def calcular_total_pago(pago_sin_inpuesto,inpuesto):
    pago_total = pago_sin_inpuesto + pago_sin_inpuesto * (inpuesto/100)
    return pago_total
# Ejecutamos la funcion 
pago_sin_Inpuesto = float(input("Digite el pago sin inpuestos "))
inpuesto = float(input("Digite el monto del inpuesto a aplicar"))
pago_con_inpuesto = calcular_total_pago(pago_sin_Inpuesto , inpuesto)
print(f"El pago con inpuesto es: {pago_con_inpuesto} ")
print("Hello Word")