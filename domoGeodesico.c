/*
 Calcular las medidas de las piezas de un domo geodesico dado su frecuencia
 */
#include <stdio.h>
#include <math.h>

struct punto2D{
   double  x;
   double  y;
};

struct punto3D{
   double  x;
   double  y;
   double  z;
};

struct punto2D puntoMedio(struct punto2D inicio, struct punto2D final, unsigned int frecuencia, unsigned int pos)
{
    if(pos == 0){
        return inicio;
    }

    if(pos == frecuencia){
        return final;
    }

    struct punto2D punto;

    double aux = pos/frecuencia;

    punto.x = aux*final.x+(1-aux)*inicio.x;
    punto.y = aux*final.y+(1-aux)*inicio.y;

    return punto;
}

double distancia3D(double x, double y, double z)
{
    return sqrt(x*x+y*y+z*z);
}

struct punto3D proyectarPunto(struct punto2D puntoPlano, unsigned int poliedro, const double alturaCara[3])
{
    double t = 1/distancia3D(puntoPlano.x, puntoPlano.y, alturaCara[poliedro]);

    struct punto3D puntoEsfera;
    puntoEsfera.x = puntoPlano.x*t;
    puntoEsfera.y = puntoPlano.y*t;
    puntoEsfera.z = alturaCara[poliedro]*t;

    return puntoEsfera;
}

int main()
{
    const double alturaCara[] = {0.2041241452,0.4082482905,0.7557613141}; //Tetraedro, Octaedro, Icosaedro de arista de longitud 1

    //En el futuro introducir mas parametros como si solo calcular medio domo, el tipo de junta, el tipo de arista, ...
    unsigned int frecuencia = 0;
    int frecuenciaAux = 0;
    float radio = 0;
    unsigned int poliedro = 0;
    int poliedroAux = 0;

    int booleano = 0;

    while(booleano != 1)
    {
        printf("Introduce la frecuencia deseada: ");
        scanf("%i", &frecuenciaAux);

        while(frecuenciaAux <= 0)
        {
            printf("Esa frecuencia no existe. Por favor, inténtelo de nuevo ");
            printf("\nIntroduce la frecuencia deseada: ");
            scanf("%i", &frecuenciaAux);
        }

        frecuencia = frecuenciaAux;

        printf("Introduce el radio de la esfera circunscrita: ");
        scanf("%f", &radio);

        while(radio <= 0)
        {
            printf("Ese radio no existe. Por favor, inténtelo de nuevo ");
            printf("\nIntroduce el radio de la esfera circunscrita: ");
            scanf("%f", &radio);
        }

        printf("Introduce el poliedro semilla Tetraedro(0), Octaedro(1), Icosaedro(2): ");
        scanf("%i", &poliedroAux);

        while(poliedroAux < 0 || poliedroAux > 2)
        {
            printf("Ese poliedro no existe. Por favor, inténtelo de nuevo ");
            printf("\nIntroduce el poliedro semilla Tetraedro(0), Octaedro(1), Icosaedro(2): ");
            scanf("%i", &poliedroAux);
        }

        poliedro = poliedroAux;

        printf("\n\nFrecuencia: %i", frecuencia);
        printf("\nRadio: %f", radio);
        printf("\npoliedro: %i", poliedro);
        printf("\n\nDesea cambiar los datos? Si(0) No(1) ");
        scanf("%i", &booleano);
        printf("\n\n\n----------------------------------------------------------------------------------------------------\n\n\n");
    }

    //Para la siguiente version aprovechar las simetrias del triangulo para calcular menos puntos

    struct punto3D caraProyectada[(int)(frecuencia*frecuencia+3*frecuencia+2)/2];

    unsigned int cont = 0;

    for(int i = 0; i <= frecuencia; i++){
        printf("i: %i", i);
        struct punto2D inicio, final;
        double y = 0.8660254038*i/frecuencia;
        inicio.y = y;
        final.y = y;
        y = i/(2*frecuencia);
        inicio.x = y;
        y = (2*frecuencia-i)/(2*frecuencia);
        final.x = y;
        printf("\ninicio.x: %f", inicio.x);
        printf("\ninicio.y: %f", inicio.y);
        printf("\nfinal.x: %f", final.x);
        printf("\nfinal.y: %f", final.y);
        printf("\n\n");
        for(int j = 0; j <= frecuencia-i; j++){
            struct punto2D aux = puntoMedio(inicio, final, frecuencia-i, j);
            printf("\nj: %i", j);
            printf("\npunto.x: %f", aux.x);
            printf("\npunto.y: %f", aux.y);
            printf("\n\n");
            caraProyectada[cont] = proyectarPunto(puntoMedio(inicio, final, frecuencia-i, j), poliedro, alturaCara);
            cont++;
        }
    }

    return 0;

}
