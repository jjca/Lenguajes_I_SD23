import java.util.Scanner;

public class rotar_1b {
    public static void main(String[] args) {
        // Creamos el scanner para recibir el input del usuario
        Scanner ku = new Scanner(System.in); 
        System.out.println("Hola, por favor introduzca su string:");
        String go = ku.nextLine();
        // Recibimos k
        System.out.println("Por favor introduzca su k:");
        Integer k = Integer.parseInt(ku.nextLine());
        // Llamamos a la función al imprimir
        System.out.println(rotar(go,k));
    }
    
    private static String rotar(String w, Integer k) {
        // Verificamos si k es menor a 0
        if (k < 0){
            System.out.println("Error: k es negativo");
            return "";
        }
        // Verificamos si k es 0 o la longitud de la cadena es 0
        else if (k == 0 || w.length() == 0) {
            return w;
        }
        else {
            // Para el 3er caso, se llama recursivamente a la funcion rotar
            String x = rotar(w.substring(1)+w.charAt(0),k-1);
            return x;
        }   
    }
}