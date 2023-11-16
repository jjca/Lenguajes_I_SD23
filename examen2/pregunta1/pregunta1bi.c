#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Church Church;
struct Church {
    struct Church* sucesor;
    char *valor;
};

Church* sucesor(Church* a)
{
    printf("hola\n");
    Church *b = NULL;
    b = (Church*)malloc(sizeof(Church));
    a->sucesor = b;
    printf("UWU");
    char *av = a->valor;
    printf("%s \n",av);
    char *tmp = (char*)malloc(strlen(av));
    char *tmp2 = ")";
    char *base = "Suc(";
    strcat(tmp,"Suc(");
    strncat(tmp,av,strlen(av));
    strcat(tmp,")");
    b->valor = (char*)malloc(strlen(tmp));
    strncpy(b->valor,tmp,strlen(tmp));
    free(tmp);
    //strncat(tmp,tmp2,1);
    //strncat(b->valor,tmp,sizeof(tmp));
    printf("El valor del retornado es: %s\n",b->valor);
    //Church *suca = a->sucesor;
    //printf("el sucesor de %s es %s \n",a->valor,suca->valor);
    return b;
}

/* Church sucesor (Church *a) {
    Church b = {NULL,NULL};
    //printf("el valor %s\n",sizeof(a.valor));
    a.sucesor = &b;
    char tmp[36] = "Suc(";
    char *tmp2 = ")";
    strncat(tmp,a.valor,sizeof(tmp));
    strncat(tmp,tmp2,1);
    strncat(b.valor,tmp,sizeof(tmp));
    printf("El valor del retornado es: %s\n",b.valor);
    Church *suca = a.sucesor;
    printf("el sucesor de %s es %s \n",a.valor,suca->valor);
    return b;
} */

Church* sucesorn (int n, Church* a)
{
    Church *b = NULL;
    b = (Church*)malloc(sizeof(Church));
    b = sucesor(a);
    printf("valor de b: %s\n",b->valor);
    for (int i = 0; i < n; i++)
        {
            b = sucesor(b);
        };
    printf("Uwito %s\n",b->valor);
    printf("el sucesor es %s\n",b->sucesor);
    return b;
}
/*
Church sumaChurch (Church a, Church b)
{
    Church *res = NULL;
    res = (Church*)malloc(sizeof(Church));
    if (a.sucesor == NULL)
    {
        res.sucesor->sucesor(b);
    }
    else if (b.sucesor == NULL)
    {
        res.sucesor = sucesor(a);
    }
    else
    {
        res.sucesor(sumaChurch(sucesor(a),b)
    }

}*/

int main() {
    Church *zero = NULL;
    zero = (Church*)malloc(sizeof(Church));
    zero->valor = "zero";
    printf("El valor de cero es: %s\n",zero->valor);
    char *a = zero->valor;
    printf("%s \n",a);
    char *tmp = (char*)malloc(strlen(a)+4);
    char *tmp2 = ")";
    char *base = "Suc(";
    strncat(tmp,base,4);
    strncat(tmp,a,strlen(a));
    strncat(tmp,tmp2,1);
    printf("jklfas %s\n",tmp);
    /* char tmp[36] = "Suc(";
    char *tmp2 = ")";
    strncat(tmp,a.valor,sizeof(tmp));
    strncat(tmp,tmp2,1);
    strncat(b.valor,tmp,sizeof(tmp)); */
    Church *uno = sucesor(zero);
    printf("El sucesor de zero es: %p\n",&zero->sucesor);
    printf("El valor del sucesor de cero es %s\n",uno->valor);
    /*Church *dos = sucesor(uno); 
    Church *tres = sucesor(dos);
    Church *cuatro = sucesor(tres);
    printf("El valor de cero es %s\n",zero->valor);
    printf("El sucesor de cero es: %s y su valor es: %s \n",zero->sucesor,uno->valor);
    printf("El sucesor de uno es: %s\n",uno->sucesor);
    printf("El valor de uno es: %s\n",uno->valor);
    printf("El valor de dos es: %s\n",dos->valor);*/
    sucesorn(5,zero);
    //printf("%d \n",zero.zero);
    return 0;
}