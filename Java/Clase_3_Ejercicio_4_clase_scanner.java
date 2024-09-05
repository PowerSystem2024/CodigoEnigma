//Ejercicio Nº4: Pedir numeros hasta que se teclee uno negativo , y mostrar cuantos numeros se han introducido.
//Clase Scanner:

import java.util.Scanner;

public class Clase_3_Ejercicio_4_clase_scanner{
      public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        int numero, conteo = 0 ;
        System.out.println("Digite un numero:");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0){
            System.out.println("El numero "+numero+ "es POSITIVO");
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("A ingresado "+conteo+" numeros que no son negativos ");
      }
}