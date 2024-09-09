/*Ejercicio 3: Leer numeros hasta que se introduzca un cero para cada uno indicar si es par o impar 
Clase scanner:
 */
//package Clase_3_Ejercicio_con_Ciclos_scanner;

import java.util.Scanner;

public class Clase_3_Ejercicio_con_Ciclos_scanner{
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0){
            if (numero % 2 == 0) {
                System.out.println("El numero ingresado " +numero+  "es PAR");
            }
            else{
                System.out.println("El numero ingresado" +numero+  "es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado es " +numero+  "finaliza el programa");

    }
}
