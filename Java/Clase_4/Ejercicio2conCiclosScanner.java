// Ejercicio Nº2: Pedir numeros hasta que se introduzca uno negativo y calcular 
//la media
package Clase_4;

import java.util.Scanner;

public class Ejercicio2conCiclosScanner {
    public static void main(final String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0 , suma = 0;
        float promedio = 0;
        System.out.println("Digite un numero: ");
        Object entrada;
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){ //mientras el numero no sea negativo
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());

    }
    if(conteo == 0);{
           System.out.println(" Error , la division entre cero no existe ");
    }
    else{
        promedio = (float)suma/conteo;
        System.out.println("El promedio es: "+promedio);
    }
    }
}
