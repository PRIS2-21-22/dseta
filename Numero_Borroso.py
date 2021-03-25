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
    def suma(self, numdifuso):

        if len(numdifuso.matriz) < 2 or len(numdifuso.matriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        if len(numdifuso.matriz) == len(self.matriz):

            if len(numdifuso.matriz) == 4:
                return NumeroDifuso(self.matriz[0] + numdifuso.matriz[0], self.matriz[1] + numdifuso.matriz[1],
                                    self.matriz[2] + numdifuso.matriz[2],self.matriz[3] + numdifuso.matriz[3])
            else:
                return NumeroDifuso(self.matriz[0]+numdifuso.matriz[0], self.matriz[1]+numdifuso.matriz[1],
                                    self.matriz[2]+numdifuso.matriz[2])

        elif len(numdifuso) == 4:
            return NumeroDifuso(self.matriz[0] + numdifuso.matriz[0], self.matriz[1] + numdifuso.matriz[1],
                                self.matriz[2] + numdifuso.matriz[2])

        else:
            return NumeroDifuso(self.matriz[0] + numdifuso.matriz[0], self.matriz[1] + numdifuso.matriz[1],
                                self.matriz[2] + numdifuso.matriz[2],  self.matriz[3] + numdifuso.matriz[2])


    # Método para restar dos numeros difusos
    def resta(self, numdifuso):

        if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        if len(numdifuso.matriz) == len(self.matriz):

            if len(numdifuso.matriz) == 4:
                return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                    self.matriz[2] - numdifuso.matriz[2], self.matriz[3] - numdifuso.matriz[3])
            else:
                return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                    self.matriz[2] - numdifuso.matriz[2])
        elif len(numdifuso) == 4:
            return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                self.matriz[2] - numdifuso[2])
        else:
            return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                self.matriz[2] - numdifuso.matriz[2], self.matriz[3] - numdifuso.matriz[2])

    # Método para hacer el opuesto de un numero difuso
    def opuesto(self, numdifuso):

        if len(numdifuso.matriz, ) > 3:
            return NumeroDifuso(-numdifuso.matriz[0], numdifuso.matriz[1], numdifuso.matriz[2], numdifuso.matriz[3])

        return NumeroDifuso(-numdifuso.matriz[0], numdifuso.matriz[1], numdifuso.matriz[2])


    # Método para multiplicar un numero difuso
    def multiplicacion(self, numdifuso):
        if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        if len(numdifuso.matriz) == len(self.matriz):

            if len(numdifuso.matriz) == 4:
                return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                    self.matriz[2] - numdifuso.matriz[2], self.matriz[3] - numdifuso.matriz[3])
            else:
                return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                    self.matriz[2] - numdifuso.matriz[2])
        elif len(numdifuso) == 4:
            return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                self.matriz[2] - numdifuso[2])
        else:
            return NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                self.matriz[2] - numdifuso.matriz[2], self.matriz[3] - numdifuso.matriz[2])
#       if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
           # Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

#        if len(self.matriz) == len(numdifuso.matriz):
        #
        #   if len(numdifuso.matriz) == 4:
        #       return NumeroDifuso(self.matriz[0]*numdifuso.matriz[0], self.matriz[1]*numdifuso.matriz[1],
        #                           self.matriz[2]*numdifuso.matriz[2], self.matriz[3]*numdifuso.matriz[3])
        #   else:
        #       return NumeroDifuso(self.matriz[0]*numdifuso.matriz[0], self.matriz[1]*numdifuso.matriz[1],
        #                           self.matriz[2]*numdifuso.matriz[2])
#        elif len(numdifuso) == 4:
#            return NumeroDifuso(self.matriz[0]*numdifuso.matriz[0], self.matriz[1]*numdifuso.matriz[1],
#                                self.matriz[2]*numdifuso.matriz[2])
#       else:
#           return NumeroDifuso(self.matriz[0]*numdifuso.matriz[0], self.matriz[1]*numdifuso.matriz[1],
    #                               self.matriz[2]*numdifuso.matriz[2], self.matriz[3]*numdifuso.matriz[2])

    # Método para dividir numero difuso
    def division(self, numdifuso):

        if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
            Exception("La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4")

        for elemento in numdifuso.matriz:
            if elemento == 0:
                Exception("Uno de los elementos es un cero")

        numdifuso_trans = NumeroDifuso(1/numdifuso.matriz[0], 1/numdifuso.matriz[1], 1/numdifuso.matriz[2],
                           1/numdifuso.matriz[3])
        # Transformamos la matriz para que cada elemento tenga su inverso
        if len(numdifuso.matriz) == 3:
            numdifuso_trans = [1/numdifuso.matriz[0], 1/numdifuso.matriz[1], 1/numdifuso.matriz[2]]

        return self.multiplicacion(numdifuso_trans)

    def tostring(self):
        print(self.matriz)



numdif = NumeroDifuso(fac=1, b=2, c=3, d=4)
numdif_secundario = NumeroDifuso(fac=1, b=2, c=3, d=4)

numdif_suma = numdif.suma(numdif_secundario)
print(numdif_suma.tostring())

numdif_resta = numdif.resta(numdif_secundario)
print(numdif_resta.tostring())

numdif_mult = numdif.multiplicacion(numdif_secundario)
print(numdif_mult.tostring())

numdif_inv = numdif.opuesto(numdif_secundario)
print(numdif_inv.tostring())

numdif_div = numdif.division(numdif_secundario)
print(numdif_div.tostring())
