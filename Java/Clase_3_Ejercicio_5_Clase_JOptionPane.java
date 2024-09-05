
/*
Ejercicio 5: Realizar un juego para adivinar un numero para ello generar un numero aleatorio entre 0-100
y luegoir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor con respecto a N
l proceso termina cuando el usuario acierta y mostramos el numero de intentos hechos.
 */

import javax.swing.JOptionPane;

public class Clase_3_Ejercicio_5_Clase_JOptionPane {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0 ;
        aleatorio = (int) (Math.random()*100); // esto genera un numero aleatorio de 0 a 100
        do{
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero mayor ");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero menor ");
            }
            else{
                JOptionPane.showMessageDialog(null,"FELICIDADES has adivinado el numero");
            }
            conteo++;

        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste el numero en: "+conteo+" intentos");
    }
}
