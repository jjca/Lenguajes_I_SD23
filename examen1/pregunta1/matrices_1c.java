import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Math;

public class matrices_1c {
    public static void main(String[] args) {
        // Creamos el scanner para recibir el input del usuario
        Scanner size = new Scanner(System.in); 
        System.out.println("Hola, por favor introduzca el tamaño de su matriz:");
        Integer k = Integer.parseInt(size.nextLine());
        // Se crea la matriz usando la estructura ArrayList de Java. Esto genera una lista con espacios vacios
        ArrayList<ArrayList<Integer>> matrizA = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < k; i++)
        {   
            // En esta linea se genera la lista dentro de cada i-esima lista para formar la matriz.
            matrizA.add(new ArrayList<Integer>());
        };

        // Inicializamos la matriz con números aleatorios entre 0 y 9
        for (int i = 0; i < matrizA.size(); i++)
        {
              for (int j = 0; j < matrizA.size(); j++)
                {   
                    matrizA.get(i).add((int)(Math.random()*10));
                }
        };
        // Imprimimos la matriz
        System.out.println("Matriz A");
        for (int i = 0; i < matrizA.size(); i++)
        {
            System.out.println(matrizA.get(i));
        };
        // Se crea la la instancia para la Transpuesta
        ArrayList<ArrayList<Integer>> matrizAt = new ArrayList<ArrayList<Integer>>();
        System.out.println("Matriz transpuesta");
        // Se llama a la función transponer
        matrizAt = Transponer(matrizA);
        // Se llama a la función multiplicar
        System.out.println("Resultado del producto AxAT");
        multiplicaMatrices(matrizA,matrizAt);
    }
    
    private static ArrayList<ArrayList<Integer>> multiplicaMatrices(ArrayList<ArrayList<Integer>> matrizA, ArrayList<ArrayList<Integer>> matrizB) {
        /*  Esta función recibe como argumento dos matrices, en este caso MatrizA y MatrizB
            Se consideran las matrices de enteros.
        */
        // Se inicializa la matriz resultante en este caso matrizC
        ArrayList<ArrayList<Integer>> matrizC = new ArrayList<ArrayList<Integer>>();
        // La variable valor es la que llevará la suma de la multiplicación
        Integer valor = 0;
        // Inicializa la matriz C
        for (int i = 0; i < matrizA.size(); i++){
            matrizC.add(new ArrayList<Integer>());
        };
        // Se añaden 0s a la matriz C. Igualmente estos valores serán reemplazados
        for (int i = 0; i < matrizA.size(); i++){
            for (int j = 0; j < matrizA.size(); j++)
                {   
                    matrizC.get(i).add(0);
                }
        };

        for (int i = 0; i < matrizC.size(); i++)
        {
            for (int j = 0; j < matrizC.size(); j++)
                {   
                    for (int k = 0; k < matrizC.size(); k++)
                    {
                        // El valor es calculado por la suma de k desde 0 a N de los elementos A[i][k]*B[k][j] 
                        valor = matrizA.get(i).get(k)*matrizB.get(k).get(j) + valor;
                    }
                    matrizC.get(i).set(j,valor);
                    valor = 0;
                }
        };
        // imprime la matriz
        for (int i = 0; i < matrizC.size(); i++)
            {
                System.out.println(matrizC.get(i));
            };
        return matrizC;
    };

    private static ArrayList<ArrayList<Integer>> Transponer(ArrayList<ArrayList<Integer>> matriz) {
        // Se inicializa la matriz Transpuesta resultante
        ArrayList<ArrayList<Integer>> matrizT = new ArrayList<ArrayList<Integer>>();
        
        for (int i = 0; i < matriz.size(); i++)
        {
            matrizT.add(new ArrayList<Integer>());
        };
        // Se establece en 0 todos los elementos de la matriz
        for (int i = 0; i < matriz.size(); i++)
        {
            for (int j = 0; j < matriz.size(); j++)
                {   
                    matrizT.get(i).add(0);
                }
        };
        // Se reemplazan los elementos de la matriz A[i][j] en AT[j][i]
        for (int i = 0; i < matriz.size(); i++)
        {
            for (int j = 0; j < matriz.size(); j++)
                {              
                    matrizT.get(i).set(j,matriz.get(j).get(i));
                }
        };
        // Imprime y retornas
        for (int i = 0; i < matrizT.size(); i++)
            {
                System.out.println(matrizT.get(i));
            };
        return matrizT;
    };
}