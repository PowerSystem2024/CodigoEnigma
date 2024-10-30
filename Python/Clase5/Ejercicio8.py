# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# inicial de 1000$ y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuentta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000
while True:
    print('\t. :MENÚ: .')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Ingrese una opción del menú'))
    print()
    if opcion == 1:
        extra = float(input('Cuánto dinero vas a ingresar -> '))
        saldo += extra
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 2:
        retirar = float(input('Cuánto dinero vas a retirar -> '))
        if retirar > saldo:
            print('Error. No tenés esa cantidad de dinero.')
        else:
            saldo -= retirar
            print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 3:
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 4:
        print('Sesión finalizada.')
        break
    else:
        print('Número ingresado incorrecto.')
        print()