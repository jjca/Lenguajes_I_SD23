#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Nodo Nodo;

struct Nodo {
    struct Nodo* hijoIzq;
    struct Nodo* hijoDer;
    int valor;
};

Nodo* nuevoNodo(int valor)
{
    Nodo *nodo = (Nodo*)malloc(sizeof(Nodo));
    nodo->valor = valor;
    nodo->hijoDer = NULL;
    nodo->hijoIzq = NULL;
    return nodo;
}

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
    Nodo *root = NULL;
    root = nuevoNodo(8);
    printf("Caso trivial: sólo hay un nodo\n");
    int tamanoArbol = conteoNodos(root);
    int *orden_preorder = (int*)malloc(tamanoArbol*sizeof(int));
    int index = 0;

    recorridoPreorder(root, orden_preorder, &index);

    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d \n",orden_preorder[i]);
    }
    
    printf("\n\n");
    index = 0;
    
    int *orden_postorder = (int*)malloc(tamanoArbol*sizeof(int));
    recorridoPostorder(root, orden_postorder, &index);
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d \n",orden_postorder[i]);
    }
    int iguales = esSimetrico(orden_preorder,orden_postorder,tamanoArbol);
    printf("Son iguales? %d \n",iguales);
    free(orden_preorder);
    free(orden_postorder);
    //////////////////////////////////////////
    printf("Caso dos: todos los nodos tienen el mismo valor\n");
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
    recorridoPreorder(root, orden_preorder, &index);

    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d \n",orden_preorder[i]);
    }
    
    printf("\n\n");
    index = 0;
   
    recorridoPostorder(root, orden_postorder, &index);
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d \n",orden_postorder[i]);
    }
    iguales = esSimetrico(orden_preorder,orden_postorder,tamanoArbol);
    printf("Son iguales? %d \n",iguales);
    free(orden_preorder);
    free(orden_postorder);


    //////////////////////////////////////////
    printf("Caso tres: todos los nodos diferentes. Este caso NO es simetrico\n");
    free(root);
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
    recorridoPreorder(root, orden_preorder, &index);

    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d \n",orden_preorder[i]);
    }
    
    printf("\n\n");
    index = 0;
   
    recorridoPostorder(root, orden_postorder, &index);
    for (int i = 0; i < tamanoArbol; i++)
    {
        printf("%d \n",orden_postorder[i]);
    }
    iguales = esSimetrico(orden_preorder,orden_postorder,tamanoArbol);
    printf("Son iguales? %d \n",iguales);
    free(orden_preorder);
    free(orden_postorder);
    return 0;
}