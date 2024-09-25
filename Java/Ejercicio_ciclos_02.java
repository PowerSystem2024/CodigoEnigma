/* Ejercicio Nº2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un cero 
este esta echo en la clase scanner falta en la clase JOPtionPane
*/
//package Ciclo_while_for_break_continue_etiquetas;

import java.util.Scanner;

public class Ejercicio_ciclos_02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0 ){
            if(numero > 0){
                System.out.println("El numero "+numero+ " es POSITIVO");
            }
          else{
            System.out.println("El numero "+numero+ "es NEGATIVO");

          }
          System.out.println("Digite otro numero: ");
          numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero "+numero+ " finaliza el programa");
    }

}