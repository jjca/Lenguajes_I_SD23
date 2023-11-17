#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Church Church;
struct Church {
    struct Church* sucesor;
    char *valor;
    int numero;
};

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

Church *sumaChurch (Church *a, Church *b)
{
    Church *res = NULL;
    res = (Church*)malloc(sizeof(Church));
    if (a->valor == "zero")  
    {
        printf("El if");
        res = b;
    }
    else if (b->valor == "zero")
    {
        printf("Else if 1");
        res = a;
    }
    else
    {
        printf("Else\n");
        int num = a->numero+b->numero;
        res = sucesorn(num-1);
    }
    return res;
}

Church *multChurch (Church *a, Church *b)
{
    Church *res = NULL;
    res = (Church*)malloc(sizeof(Church));
    if (a->valor == "zero")  
    {
        printf("El if");
        res = a;
    }
    else if (b->valor == "zero")
    {
        res = b;
    }
    else
    {
        printf("Else\n");
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
    /* char tmp[36] = "Suc(";
    char *tmp2 = ")";
    strncat(tmp,a.valor,sizeof(tmp));
    strncat(tmp,tmp2,1);
    strncat(b.valor,tmp,sizeof(tmp)); */
    Church *uno = sucesor(zero);
    printf("El sucesor de zero es: %p\n",&zero->sucesor);
    printf("El valor del sucesor de cero es %s\n",uno->valor);
    Church *dos = sucesor(uno); 
    Church *tres = sucesor(dos);
    Church *cuatro = sucesor(tres);
    Church *cinco = sucesor(cuatro);
    Church *seis = sucesor(cinco);
    Church *siete = sucesor(seis);
    /*printf("El valor de cero es %s\n",zero->valor);
    printf("El sucesor de cero es: %s y su valor es: %s \n",zero->sucesor,uno->valor);
    printf("El sucesor de uno es: %s\n",uno->sucesor);
    printf("El valor de uno es: %s\n",uno->valor);
    printf("El valor de dos es: %s\n",dos->valor);*/
    //Church *seis = sucesorn(10,zero);
    printf("Hola! %s\n",seis->valor);
    Church *suma = sumaChurch(cuatro,seis);
    printf("Rsultado de la suma: 4+6: %s\n",suma->valor);
    Church *prod = multChurch(seis,dos);
    printf("Rsultado del producto: 6*2 %s\n",prod->valor);
    //printf("%d \n",zero.zero);
    return 0;
}