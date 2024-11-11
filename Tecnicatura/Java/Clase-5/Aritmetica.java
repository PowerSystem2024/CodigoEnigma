package Clase05;

public class Aritmetica {
    int a;
    int b;

    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }

    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }

    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1;
        this.b = arg2;
        //return a + b;
        return sumarConRetorno();
    }
}
