//package Ciclo_while_for_break_continue_etiquetas;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0 ; //inferencia de tipos 
        while (conteo < 7) {
            System.out.println("conteo = "+ conteo);
            conteo++; //el incremento va aumentando en uno la variable 
            
        }
 //ciclo do while , son similares lo que cambia son como se ejecutan las lineas de codigo en el anterior 
//primero veiamos que se veia la condicion y luego lo repetia si era verdadera y si era falsa terminaba el ciclo 
// en este cxaso es totalmente diferente lo primero que lleva es el du y luego vienen las lineas de codigo 
// el ciclo du while primero ejecuta el codigo de su interior y luego hace la comprobacion , 
// en el while primero esta la comprobaciojn , si no se cumple es false 
        var contador = 0;
        do{
            System.out.println("contador = " + contador );
            contador++;

        }while(contador < 7);

         //Ciclo ford: maneja un numero determinado deiteraciones a diferencia de los ciclos while o de while que manejan
         //un numero indeterminado de iteraciones 
         //el ciclo for tiene una condicion que se debe rervisar , si es verdadera se ejecuta el codigo dentro del ciclo , si es falsa no 
         // ejecuta nada dentro del ciclo 
         //cuando la condicion se cumple este comienza un incremento o decremento hasta que la condicion sea falsa y sale 

          for(var contando = 0 ; contando< 7 ; contando++){    // tiene tres lugares , el primero lo usamos para declarar una variable de tipo contador o iterador 
               System.out.println("contando = " + contando);   // segunda parte condicion 
           }                                                   // tercera parte incremento o decremento del contador 

        
           // break:
           // brerak rompe el ciclo 
           for(var contando = 0 ; contando< 7 ; contando++){
               if(contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break; //este break rompe el ciclo y me marca solo el primer numerpo par 
            } 
              
        }     
        //continue : pide que continue el programa cuando encuentra en numero impar                                            
        for(var contando = 0 ; contando< 7 ; contando++){
            if(contando % 2 != 0) {
               continue;
            }
             System.out.println("contando = " + contando);
        }
    }
}