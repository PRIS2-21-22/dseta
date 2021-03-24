import sys

class NumeroDifuso:

    # Matriz que representa el numero difuso
    matriz = []

    # Metodo para iniciar la clase
    def __init__(self, fac:float, b:float, c:float, d: float):
       if d == None:
           self.matriz = [fac, b, c]
       else:
           self.matriz = [fac, b, c, d]

    # Método para sumar dos numeros difusos
    def suma(self, otramatriz: list):

        if len(otramatriz) < 2 or len(otramatriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        if len(otramatriz) == len(self.matriz):

            if(len(otramatriz)== 4):
                return NumeroDifuso(self.matriz[0] + otramatriz[0], self.matriz[1] + otramatriz[1],
                                    self.matriz[2] + otramatriz[2],self.matriz[3] + otramatriz[3])
            else:
                return NumeroDifuso(self.matriz[0]+otramatriz[0], self.matriz[1]+otramatriz[1],
                                    self.matriz[2]+otramatriz[2])

        elif len(otramatriz) == 4:
            return NumeroDifuso(self.matriz[0] + otramatriz[0], self.matriz[1] + otramatriz[1],
                                self.matriz[2] + otramatriz[2])

        else:
            return NumeroDifuso(self.matriz[0] + otramatriz[0], self.matriz[1] + otramatriz[1],
                                self.matriz[2] + otramatriz[2],  self.matriz[3] + otramatriz[2])



    # Método para restar dos numeros difusos
    def resta(self, otramatriz: list):

        if len(otramatriz) <= 2 or len(otramatriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        if len(otramatriz) == len(self.matriz):

            if (len(otramatriz) == 4):
                return NumeroDifuso(self.matriz[0] - otramatriz[0], self.matriz[1] - otramatriz[1],
                                    self.matriz[2] - otramatriz[2], self.matriz[3] - otramatriz[3])
            else:
                return NumeroDifuso(self.matriz[0] - otramatriz[0], self.matriz[1] - otramatriz[1],
                                    self.matriz[2] - otramatriz[2])
        elif len(otramatriz) == 4:
            return NumeroDifuso(self.matriz[0] - otramatriz[0], self.matriz[1] - otramatriz[1],
                                self.matriz[2] - otramatriz[2])
        else:
            return NumeroDifuso(self.matriz[0] - otramatriz[0], self.matriz[1] - otramatriz[1],
                                self.matriz[2] - otramatriz[2], self.matriz[3] - otramatriz[2])

    # Método para hacer el opuesto de un numero difuso
    def opuesto(self):

        if len(self.matriz, ) > 3:
            return NumeroDifuso(-self.matriz[0], self.matriz[1], self.matriz[2], self.matriz[3])

        return NumeroDifuso(-self.matriz[0], self.matriz[1], self.matriz[2])


    # Método para multiplicar un numero difuso
    def multiplicacion(self, otramatriz: list):

        if len(otramatriz) <= 2 or len(otramatriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        if len(otramatriz) == len(self.matriz):

            if (len(otramatriz) == 4):
                return NumeroDifuso(self.matriz[0] * otramatriz[0], self.matriz[1] * otramatriz[1],
                                    self.matriz[2] * otramatriz[2], self.matriz[3] * otramatriz[3])
            else:
                return NumeroDifuso(self.matriz[0] * otramatriz[0], self.matriz[1] * otramatriz[1],
                                    self.matriz[2] * otramatriz[2])
        elif len(otramatriz) == 4:
            return NumeroDifuso(self.matriz[0] * otramatriz[0], self.matriz[1] * otramatriz[1],
                                self.matriz[2] * otramatriz[2])
        else:
            return NumeroDifuso(self.matriz[0] * otramatriz[0], self.matriz[1] * otramatriz[1],
                                self.matriz[2] * otramatriz[2], self.matriz[3] * otramatriz[2])

    # Método para dividir numero difuso
    def division(self, otramatriz: list):

        if len(otramatriz) <= 2 or len(otramatriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        for elemento in otramatriz:
            if elemento == 0:
                Exception("Uno de los elementos es un cero")

        otramatriz_trans = []

        # Transformamos la matriz para que cada elemento tenga su inverso
        if len(otramatriz) == 3:
            otramatriz_trans = [1/otramatriz[0], 1/otramatriz[1], 1/otramatriz/[2]]
        else:
            otramatriz_trans = [1/otramatriz[0], 1/otramatriz[1], 1/otramatriz/[2], 1/otramatriz/[3]]

        return self.multiplicacion(self, otramatriz_trans)

