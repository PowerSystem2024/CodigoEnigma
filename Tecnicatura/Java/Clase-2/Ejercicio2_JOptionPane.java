import javax.swing.JOptionPane;

public class Ejercicio2_JOptionPane {
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
