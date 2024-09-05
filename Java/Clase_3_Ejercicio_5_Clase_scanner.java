/*
Ejercicio 5: Realizar un juego para adivinar un numero para ello generar un numero aleatorio entre 0-100
y luegoir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor con respecto a N
l proceso termina cuando el usuario acierta y mostramos el numero de intentos hechos.
 */

import java.util.Scanner;

public class Clase_3_Ejercicio_5_Clase_scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0 ;
        aleatorio = (int) (Math.random()*100); // esto genera un numero aleatorio de 0 a 100
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor ");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor ");
            }
            else{
                System.out.println("FELICIDADES has adivinado el numero");
            }
            conteo++;

        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: "+conteo+" intentos");

    }
}
