import math

class punto2D:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__():
        return "("+self.x+", "+self.y+")"

class punto3D:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__():
        return "("+self.x+", "+self.y+", "+self.z+")"

class domo:
    alturaCara = [0.2041241452,0.4082482905,0.7557613141]
    h = 0.8660254038
    puntos = []
    aristas = []
    frecuencia = 0
    radio = 0
    poliedro = 0

    def __init__(self):
        booleano = False
        while(booleano != 1):

            self.frecuencia = int(input("Introduce la frecuencia deseada: "))
            while(self.frecuencia <= 0):
                print("Esa frecuencia no existe. Por favor, inténtelo de nuevo ")
                self.frecuencia = int(input("Introduce la frecuencia deseada: "))

            self.radio = int(input("Introduce el radio deseado: "))
            while(self.radio <= 0):
                print("Ese radio no existe. Por favor, inténtelo de nuevo ")
                self.radio = int(input("Introduce el radio deseado: "))

            self.poliedro = int(input("Introduce el poliedro semilla Tetraedro(0), Octaedro(1), Icosaedro(2): "))
            while(self.poliedro < 0 or self.poliedro > 2):
                print("Ese poliedro no existe. Por favor, inténtelo de nuevo ")
                self.poliedro = int(input("Introduce el poliedro semilla Tetraedro(0), Octaedro(1), Icosaedro(2): "))

            print("\nFrecuencia: " + str(self.frecuencia))
            print("Radio: " + str(self.radio))
            print("poliedro: " + str(self.poliedro))
            booleano = int(input("\nDesea cambiar los datos? Si(0) No(1) "))
            print("\n\n\n----------------------------------------------------------------------------------------------------\n\n\n")

        self.proyectarEsfera()

    def puntoMedio(self, inicio, final, frecuencia, pos):
        if frecuencia == 0:
            return inicio
        aux = pos/frecuencia
        return punto2D(aux*final.x+(1-aux)*inicio.x, aux*final.y+(1-aux)*inicio.y)

    def distancia3D(self, x, y, z):
        return math.sqrt(x*x+y*y+z*z)

    def proyectarPunto(self, puntoPlano, poliedro, alturaCara):
        t = 1/self.distancia3D(puntoPlano.x, puntoPlano.y, alturaCara[poliedro])
        return punto3D(self.radio*puntoPlano.x*t, self.radio*puntoPlano.y*t, self.radio*alturaCara[poliedro]*t)

    def proyectarEsfera(self):
        for i in range(self.frecuencia+1):
            inicio = punto2D(i/(2*self.frecuencia)-0.5, (self.h*i/self.frecuencia)-self.h/3)
            final = punto2D(((2*self.frecuencia-i)/(2*self.frecuencia))-0.5, (self.h*i/self.frecuencia)-self.h/3)
            for j in range(self.frecuencia+1-i):
                self.puntos.append(self.proyectarPunto(self.puntoMedio(inicio, final, self.frecuencia-i, j), self.poliedro, self.alturaCara))

    def calcularAristas(self):
        count = 0
        for i in range(self.frecuencia):
            for j in range(self.frecuencia+1-i):
                if j == 0:
                    aristas.append(self.distancia3D(puntos[count].x-puntos[count+self.frecuencia+1-i].x,self.distancia3D(puntos[count].y-puntos[count+self.frecuencia+1-i].y,self.distancia3D(puntos[count].z-puntos[count+self.frecuencia+1-i].z)) #distancia arriba a la derecha
                    aristas.append(self.distancia3D(puntos[count].x-puntos[count+1].x,self.distancia3D(puntos[count].y-puntos[count+1].y,self.distancia3D(puntos[count].z-puntos[count+1].z)) #distancia abajo a la derecha
                else if j == self.frecuencia-i:
                    aristas.append(self.distancia3D(puntos[count].x-puntos[count+self.frecuencia-i].x,self.distancia3D(puntos[count].y-puntos[count+self.frecuencia-i].y,self.distancia3D(puntos[count].z-puntos[count+self.frecuencia-i].z)) #distancia arriba a la izquierda
                else if j != 0 and j != self.frecuencia-i:
                    aristas.append(self.distancia3D(puntos[count].x-puntos[count+self.frecuencia+1-i].x,self.distancia3D(puntos[count].y-puntos[count+self.frecuencia+1-i].y,self.distancia3D(puntos[count].z-puntos[count+self.frecuencia+1-i].z)) #distancia arriba a la derecha
                    aristas.append(self.distancia3D(puntos[count].x-puntos[count+self.frecuencia-i].x,self.distancia3D(puntos[count].y-puntos[count+self.frecuencia-i].y,self.distancia3D(puntos[count].z-puntos[count+self.frecuencia-i].z)) #distancia arriba a la izquierda
                    aristas.append(self.distancia3D(puntos[count].x-puntos[count+1].x,self.distancia3D(puntos[count].y-puntos[count+1].y,self.distancia3D(puntos[count].z-puntos[count+1].z)) #distancia abajo a la derecha
                count += 1


if __name__ == '__main__':
    domo1 = domo()
