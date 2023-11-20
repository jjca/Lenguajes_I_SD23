#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Nodo Nodo;

/*
Struct que define un Nodo
Tiene dos apuntadores a nodos
y un valor
*/
struct Nodo {
    struct Nodo* hijoIzq;
    struct Nodo* hijoDer;
    int valor;
};

/*
Función que retorna un nuevo nodo en base a un valor
Este retorna un pointer de tipo nodo.
*/
Nodo* nuevoNodo(int valor)
{
    Nodo *nodo = (Nodo*)malloc(sizeof(Nodo));
    nodo->valor = valor;
    nodo->hijoDer = NULL;
    nodo->hijoIzq = NULL;
    return nodo;
}

/*
Función que cuenta la cantidad de nodos recursivamente.
Estos son contados a partir de  un nodo dado, no necesariamente cuenta aquellos nodos si el nodo dado tiene papá
*/
int conteoNodos(Nodo *nodo)
{
    if (nodo == NULL)
    {
        return 0;
    }
    int conteoIzq = conteoNodos(nodo->hijoIzq);
    int conteoDer = conteoNodos(nodo->hijoDer);

    return 1 + conteoDer + conteoIzq;

}
/*
Método para recorrer obtener recursivamente 
el preorder desde el root del árbol
*/
void recorridoPreorder(Nodo *nodo, int *array, int *index)
{
    if (nodo == NULL)
    {
        return;
    }
    array[(*index)++] = nodo->valor;
    recorridoPreorder(nodo->hijoIzq,array,index);
    recorridoPreorder(nodo->hijoDer,array,index);
}

/*
Método para recorrer obtener recursivamente 
el postorder desde el root del árbol
*/
void recorridoPostorder(Nodo *nodo, int *array, int *index)
{    
    if (nodo == NULL)
    {
        return;
    }
    recorridoPostorder(nodo->hijoIzq, array, index);
    recorridoPostorder(nodo->hijoDer, array, index);
    array[(*index)++] = nodo->valor;
}

/*
Función que retorna el valor de si es simetrico o no el árbol
*/
int esSimetrico(int *orden_preorder, int *orden_postorder,int tamanoArbol)
{
    int iguales = 1;
    for (int i = 0; i < tamanoArbol; i++)
    {
        if (orden_postorder[i] != orden_preorder[i])
        {
            iguales = 0;
            return iguales;
        }
    }
    return iguales;
}

int main() {
    // Crea un nuevo nodo como raiz
    Nodo *root = NULL;
    root = nuevoNodo(8);
    printf("Caso trivial: sólo hay un nodo\n");
    int tamanoArbol = conteoNodos(root);
    int *orden_preorder = (int*)malloc(tamanoArbol*sizeof(int));
    int index = 0;
    // Ejecuta el recorridoPreorder
    recorridoPreorder(root, orden_preorder, &index);
    // El orden es guardado en un array.
    printf("Preorder del primer árbol: \n");
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d ",orden_preorder[i]);
    }
    printf("\n\n");
    index = 0;
    int *orden_postorder = (int*)malloc(tamanoArbol*sizeof(int));
    // Recorrido postorder e inicialzación
    // se guarda en un array el resultado
    recorridoPostorder(root, orden_postorder, &index);
    printf("Postorder del primer árbol: \n");
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d ",orden_postorder[i]);
    }
    int iguales = esSimetrico(orden_preorder,orden_postorder,tamanoArbol);
    printf("\n");
    if (iguales > 0){
        printf("Son iguales \n");
    }
    else
    {
        printf("NO son iguales \n");
    }
    
    free(orden_preorder);
    free(orden_postorder);

    //////////////////////////////////////////
    printf("\n \n");
    printf("Caso dos: todos los nodos tienen el mismo valor\n");

    // Define un nuevo árbol
    free(root);
    root = nuevoNodo(5);
    root->hijoDer = nuevoNodo(5);
    root->hijoIzq = nuevoNodo(5);
    root->hijoIzq->hijoIzq = nuevoNodo(5);
    root->hijoIzq->hijoDer = nuevoNodo(5);
    root->hijoDer->hijoDer = nuevoNodo(5);
    root->hijoDer->hijoIzq = nuevoNodo(5);
    tamanoArbol = conteoNodos(root);
    index = 0;
    orden_preorder = (int*)malloc(tamanoArbol*sizeof(int));
    orden_postorder = (int*)malloc(tamanoArbol*sizeof(int));
    // Se realiza el recorrido preorder
    recorridoPreorder(root, orden_preorder, &index);
    printf("Preorder del segundo árbol: \n");
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d ",orden_preorder[i]);
    }
    
    printf("\n\n");
    index = 0;
   // Se realiza el recorrido postorder
    recorridoPostorder(root, orden_postorder, &index);
    printf("Postorder del segundo árbol: \n");
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d ",orden_postorder[i]);
    }
    iguales = esSimetrico(orden_preorder,orden_postorder,tamanoArbol);
    printf("\n");
    if (iguales > 0){
        printf("Son iguales \n");
    }
    else
    {
        printf("NO son iguales \n");
    }
    free(orden_preorder);
    free(orden_postorder);


    //////////////////////////////////////////
    printf("\n\n");
    printf("Caso tres: todos los nodos diferentes. Este caso NO es simetrico\n");
    free(root);
    // Se define un nuevo árbol
    root = nuevoNodo(8);
    root->hijoDer = nuevoNodo(5);
    root->hijoIzq = nuevoNodo(5);
    root->hijoIzq->hijoIzq = nuevoNodo(2);
    root->hijoIzq->hijoDer = nuevoNodo(3);
    root->hijoDer->hijoDer = nuevoNodo(3);
    root->hijoDer->hijoIzq = nuevoNodo(2);
    tamanoArbol = conteoNodos(root);
    index = 0;
    orden_preorder = (int*)malloc(tamanoArbol*sizeof(int));
    orden_postorder = (int*)malloc(tamanoArbol*sizeof(int));

    // Se realiza el recorrido preorder
    recorridoPreorder(root, orden_preorder, &index);
    printf("Preorder del tercer árbol: \n");
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d ",orden_preorder[i]);
    }
    
    printf("\n\n");
    index = 0;
   // Se realiza el recorrido postorder
    printf("Postorder del tercer árbol: \n");
    recorridoPostorder(root, orden_postorder, &index);
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d ",orden_postorder[i]);
    }
    iguales = esSimetrico(orden_preorder,orden_postorder,tamanoArbol);
    printf("\n");
    if (iguales > 0){
        printf("Son iguales \n");
    }
    else
    {
        printf("NO son iguales \n");
    }
    free(orden_preorder);
    free(orden_postorder);
    return 0;
}