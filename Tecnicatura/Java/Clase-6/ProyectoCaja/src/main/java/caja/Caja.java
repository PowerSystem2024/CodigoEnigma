
package caja;

public class Caja{
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Métodos y constructores (acciones)
    public Caja(){
        
    }
    public Caja(int ancho, int alto, int profundo){
       this.ancho = ancho; 
       this.alto = alto;
       this.profundo = profundo;
    }
    
    public int calcularVolumen(){
        return ancho * alto * profundo;
    }
}
