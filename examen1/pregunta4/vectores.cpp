#include "iostream"
#include "cmath"
#include "cstdlib"
using namespace std;

namespace espacioDeVectores {
    class Vector {
        public:
            float valor_x;
            float valor_y;
            float valor_z;
            Vector(float x, float y, float z) {
                valor_x = x;
                valor_y = y;
                valor_z = z;
            };
            void print() {
                cout << "(" << valor_x << "," << valor_y << "," << valor_z << ")" << endl;
            }
    };
    // Suma de vectores
    Vector operator +(const Vector& vector1, const Vector& vector2)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_x + vector2.valor_x;
        resultado.valor_y = vector1.valor_y + vector2.valor_y;
        resultado.valor_z = vector1.valor_z + vector2.valor_z;
        return resultado;
    }

    // Suma vector y float a derecha
    Vector operator +(const Vector& vector, const float& numero) 
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector.valor_x + numero;
        resultado.valor_y = vector.valor_y + numero;
        resultado.valor_z = vector.valor_z + numero;
        return resultado;
    }

    // Suma vector y float a izquierda
    Vector operator +(const float& numero, const Vector& vector) 
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector.valor_x + numero;
        resultado.valor_y = vector.valor_y + numero;
        resultado.valor_z = vector.valor_z + numero;
        return resultado;
    }
    
    // Resta de vectores
    Vector operator -(const Vector& vector1,const Vector& vector2)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_x - vector2.valor_x;
        resultado.valor_y = vector1.valor_y - vector2.valor_y;
        resultado.valor_z = vector1.valor_z - vector2.valor_z;
        return resultado;
    }

    // Producto vectorial
    Vector operator *(const Vector& vector1, const Vector& vector2)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_y*vector2.valor_z - vector2.valor_y*vector1.valor_z;
        resultado.valor_y = vector2.valor_x*vector1.valor_z-vector1.valor_x*vector2.valor_z;
        resultado.valor_z = vector1.valor_x*vector2.valor_y - vector2.valor_x*vector1.valor_y;
        return resultado;
    }

    // Producto vector con float a derecha
    Vector operator *(const Vector& vector1, const float& numero)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_x*numero;
        resultado.valor_y = vector1.valor_y*numero;
        resultado.valor_z = vector1.valor_z*numero;
        return resultado;
    }

    // Producto vector con float a izquierda
    Vector operator *(const float& numero,const Vector& vector1)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_x*numero;
        resultado.valor_y = vector1.valor_y*numero;
        resultado.valor_z = vector1.valor_z*numero;
        return resultado;
    }

    // Resta vector con float a derecha
    Vector operator -(const Vector& vector1, const float& numero)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_x-numero;
        resultado.valor_y = vector1.valor_y-numero;
        resultado.valor_z = vector1.valor_z-numero;
        return resultado;
    }

    // Resta vector con float a izquierda
    Vector operator -(const float& numero,const Vector& vector1)
    {
        Vector resultado(0,0,0);
        resultado.valor_x = vector1.valor_x-numero;
        resultado.valor_y = vector1.valor_y-numero;
        resultado.valor_z = vector1.valor_z-numero;
        return resultado;
    }

    // Producto punto
    float operator%(const Vector& vector1, const Vector& vector2) {
        float punto = vector1.valor_x*vector2.valor_x + vector1.valor_y*vector2.valor_y + vector1.valor_z*vector2.valor_z;
        return punto;
    }

    // Modulo
    float operator& (const Vector& vector) {
        float modulo = sqrt(pow(vector.valor_x,2)+pow(vector.valor_y,2)+pow(vector.valor_z,2));
        return modulo;
    }
    

};

using namespace espacioDeVectores;
int main(void) {
    std::cout << "hello world";
    Vector a(rand()%10,rand()%10,rand()%10);
    Vector b(rand()%10,rand()%10,rand()%10);
    Vector c(rand()%10,rand()%10,rand()%10);
    Vector res(0,0,0);
    float res2;
    a.print();
    b.print();
    c.print();
    res = a+b;
    cout << "a+b";
    res.print();

    res = b+a;
    cout << "b+a";
    res.print();
    
    res = a*b+c;
    cout << "a*b+c";
    res.print();
    
    res = (b+b)*(c-a);
    cout << "(b+b)*(c-a)";
    res.print();

    res = a+3;
    cout << "a+3";
    res.print();

    res = 3+a;
    cout << "3+a";
    res.print();
    //res = a % (c*b);
    res = a * 3.0 + &b;
    cout << "a*3.0+&b";
    res.print();
    res = a * 3.0 + &b;
    cout << "3.0*a+&b";
    res.print();

    res = (b+b);
    cout << "b+b";
    res.print();


    res2 = c % a;
    cout << "c%a" << res2 << endl;

    res2 = a % c;
    cout << "a%c" << res2 << endl;

    res2 = a%(c*b);
    cout << "a%(c*b)" << res2 << endl;

    res = (b+b) * (c%a);
    cout << "(b+b) * (c%a);";
    res.print();

    res = (c%a)*(b+b);
    cout << " (c%a)*(b+b);";
    res.print();

    
    return 0;
};