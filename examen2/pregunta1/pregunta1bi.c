#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Church Church;

/*
Struct que define formalmente a un número de Church
Pueden tener un valor en tipo Char, el que representa su expresión en términos de numerales de
Church. Ej: Suc(Zero)
El valor de dicho número en notación arábiga.
Sucesor como un pointer de tipo Church*
*/
struct Church {
    struct Church* sucesor;
    char *valor;
    int numero;
};


/*
Función que define un sucesor de Church.
Recibe un pointer y retorna otro pointer para el nuevo sucesor.
*/
Church* sucesor(Church* a)
{
    Church *b = NULL;
    b = (Church*)malloc(sizeof(Church));
    a->sucesor = b;
    b->numero = a->numero+1;
    char *av = (char*)malloc(sizeof(a->valor));
    av = a->valor;
    char *tmp = (char*)malloc(strlen(av)+5);
    char *tmp2 = ")";
    char *base = "Suc(";
    strncat(tmp,base,4);
    strncat(tmp,av,strlen(av));
    strncat(tmp,tmp2,1);
    b->valor = malloc(strlen(tmp));
    strncpy(b->valor,tmp,strlen(tmp));
    free(tmp);
    free(av);
    return b;
}
/*
Funcion que define el sucesor de un número n dado
Recibe un int y retorna un pointer de tipo Church con el sucesor de dicho n dado
*/
Church* sucesorn (int n)
{
    Church *zero = NULL;
    zero = (Church*)malloc(sizeof(Church));
    zero->valor = (char*)malloc(sizeof(char));
    zero->valor = "zero";
    zero->numero = 0;
    Church *b = NULL;
    b = (Church*)malloc(sizeof(Church));
    b = sucesor(zero);
    for (int i = 0; i < n; i++)
        {
            b = sucesor(b);
        };
    free(zero);
    return b;
}
/*
Función para la suma de dos numerales de Church
Recibe dos numerales, retorna un número.
*/
Church *sumaChurch (Church *a, Church *b)
{
    Church *res = NULL;
    res = (Church*)malloc(sizeof(Church));
    if (a->valor == "zero")  
    {
        res = b;
    }
    else if (b->valor == "zero")
    {
        res = a;
    }
    else
    {
        int num = a->numero+b->numero;
        res = sucesorn(num-1);
    }
    return res;
}
/*
Función para la multiplicación de dos numerales de Church. Recibe dos numerales y retorna uno.
*/
Church *multChurch (Church *a, Church *b)
{
    Church *res = NULL;
    res = (Church*)malloc(sizeof(Church));
    if (a->valor == "zero")  
    {
        res = a;
    }
    else if (b->valor == "zero")
    {
        res = b;
    }
    else
    {
        int num = a->numero*b->numero;
        res = sucesorn(num-1);
    }
    return res;
}

int main() {
    Church *zero = NULL;
    zero = (Church*)malloc(sizeof(Church));
    zero->valor = (char*)malloc(sizeof(char));
    zero->valor = "zero";
    zero->numero = 0;
    Church *uno = sucesor(zero);
    printf("El sucesor de zero es: %p\n",&zero->sucesor);
    printf("El valor del sucesor de cero es %s\n",uno->valor);
    /*
    Aqui hay números del 2 al 7 definidos como Church en base al sucesor de su predecesor, desde el cero.
    */
    Church *dos = sucesor(uno); 
    Church *tres = sucesor(dos);
    Church *cuatro = sucesor(tres);
    Church *cinco = sucesor(cuatro);
    Church *seis = sucesor(cinco);
    Church *siete = sucesor(seis);
    printf("Hola! %s\n",seis->valor);
    // Operaciones sobre estos numerales ya definidos
    Church *suma = sumaChurch(cuatro,seis);
    printf("Rsultado de la suma: 4+6: %s\n",suma->valor);
    Church *prod = multChurch(seis,dos);
    printf("Rsultado del producto: 6*2 %s\n",prod->valor);
    return 0;
}