
    /* Ejercicio Nº2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un cero 
este esta echo en la clase JOPtionPane
*/
//package Ciclo_while_for_break_continue_etiquetas;

import javax.swing.JOptionPane;

public class Ejercicio_ciclos_02_JOptionPane {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero != 0 ){
            if(numero > 0){
                 JOptionPane.showMessageDialog(null, "El numero"+numero+ "es POSITIVO");
            }
          else{
            JOptionPane.showMessageDialog(null, "El numero"+numero+ "es NEGATIVO");

          }
          numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+" Finaliza el programa");
    }
       
    }

