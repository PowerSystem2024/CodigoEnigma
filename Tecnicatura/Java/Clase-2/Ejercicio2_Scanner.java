import java.util.Scanner;

public class Ejercicio2_Scanner {
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
