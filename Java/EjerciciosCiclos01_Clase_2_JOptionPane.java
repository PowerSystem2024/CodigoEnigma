// Clase sobre JOptionpane que hace que hagamos el ejercicio mas corto y en pycharm nos abre una pestaña para poder 
//ingresar los numeros o cosas que nos piden 
// es el mismo ejerecicio que el anteriror solo que es mas corto
//package Ciclo_while_for_break_continue_etiquetas;

import javax.swing.JOptionPane;

public class EjerciciosCiclos01_Clase_2_JOptionPane {
    public static void main(String[] args){
         
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero >= 0 ) { //Minetras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+"elevado al cuadrado es:"+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
}
