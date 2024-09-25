//Ejercicio 1: leer un numero y mostrar su cuadrado , repetir el proceso hasta que se introduzca un numero negativo
//package Ciclo_while_for_break_continue_etiquetas;

import java.util.Scanner;

public class EjerciciosCiclos01_Clase_2 {
public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Digite un numero");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0 ) { //Minetras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+"elevado al cuadrado es:"+cuadrado);
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
}