#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Church Church;
struct Church {
    struct Church* sucesor;
    char *valor;
};

Church sucesor (Church a) {
    Church b = {NULL,malloc(2*sizeof(a.valor))};
    a.sucesor = &b;
    char tmp[20] = "Suc(";
    char *tmp2 = ")";
    strncat(tmp,a.valor,sizeof(tmp));
    strncat(tmp,tmp2,1);
    strncat(b.valor,tmp,sizeof(tmp));
    printf("El valor recibido es: %d\n",a.valor);
    printf("El valor del retornado es: %s\n",b.valor);
    return b;
}

Church sucesorn (int n)
{
    Church b = {NULL,malloc(2*n)};
    for (int i = 0; i < n; i++)
    {
        char tmp[20] = "Suc(";
        char *tmp2 = ")";
        strncat(tmp,(char*)&n,sizeof(tmp));
        strncat(tmp,tmp2,1);
        strncat(b.valor,tmp,sizeof(tmp));
    }
    printf("Uwito %s",b.valor);
    return b;
}

Church sumaChurch (Church a, Church b)
{

}

int main() {
    
    Church zero = {NULL,"zero"};
    Church *x = NULL;
    x = (Church*)malloc(sizeof(Church));
    
    Church y = sucesor(zero);
    Church z = sucesor(y);

    Church j = sucesor(y);

    Church uno = sucesor(zero);
    Church dos = sucesor(uno);
    printf("El valor de uno es: %s\n",uno.valor);
    printf("El valor de dos es: %s\n",dos.valor);
    sucesorn(5);
    //printf("%d \n",zero.zero);
    return 0;
}