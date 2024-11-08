package domain;

public class Persona {
    public final static int CONSTANQUE_AQUI = 15;
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
    public final void Imprimir() {
       System.out.println("Método para imprimir");
    }
}