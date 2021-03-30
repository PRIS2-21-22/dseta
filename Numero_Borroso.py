

class NumeroDifuso:
    # Matriz que representa el numero difuso
    matriz = []

    # Metodo para iniciar la clase
    def __init__ (self, fac: float, b: float, c: float, d: float):

        if d < 0:
            self.matriz = [fac, b, c]
        else:
            self.matriz = [fac, b, c, d]

    # Método para sumar dos numeros difusos
    def suma (self, numdifuso):

        if len(numdifuso.matriz) < 2 or len(numdifuso.matriz) > 4:
            self.matriz = [0, 0, 0]
            return "La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4"

        numeroDif = 1

        if len(numdifuso.matriz) == len(self.matriz):

            if len(numdifuso.matriz) == 4:
                numeroDif = NumeroDifuso(self.matriz[0] + numdifuso.matriz[0], self.matriz[1] + numdifuso.matriz[1],
                                         self.matriz[2] + numdifuso.matriz[2], self.matriz[3] + numdifuso.matriz[3])
            else:
                numeroDif = NumeroDifuso(self.matriz[0] + numdifuso.matriz[0], self.matriz[1] + numdifuso.matriz[1],
                                         self.matriz[2] + numdifuso.matriz[2], -1)
        else:
            numeroDif = NumeroDifuso(self.matriz[0] + numdifuso.matriz[0], self.matriz[1] + numdifuso.matriz[1],
                                     self.matriz[2] + numdifuso.matriz[2], self.matriz[2] + numdifuso.matriz[2])

        return numeroDif

    # Método para restar dos numeros difusos
    def resta (self, numdifuso):

        if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
            self.matriz = [0, 0, 0]
            return "La matriz que quiere sumar a la anterior debe de tener un tamaño comprendido entre 3 y 4"

        numeroDif = 1

        if len(numdifuso.matriz) == len(self.matriz):

            if len(numdifuso.matriz) == 4:
                numeroDif = NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                         self.matriz[2] - numdifuso.matriz[2], self.matriz[3] - numdifuso.matriz[3])
            else:
                numeroDif = NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                         self.matriz[2] - numdifuso.matriz[2], -1)
        else:
            numeroDif = NumeroDifuso(self.matriz[0] - numdifuso.matriz[0], self.matriz[1] - numdifuso.matriz[1],
                                     self.matriz[2] - numdifuso.matriz[2], self.matriz[2] - numdifuso.matriz[2])

        return numeroDif

    # Método para hacer el opuesto de un numero difuso

    # Método para multiplicar un numero difuso
    def multiplicacion (self, numdifuso):

        if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
            self.matriz = [0, 0, 0]
            return "La matriz debe de tener entre 3 y 4 elementos"

        numeroDif = 1

        if len(numdifuso.matriz) == len(self.matriz):

            if len(numdifuso.matriz) == 4:
                numeroDif = NumeroDifuso(self.matriz[0] * numdifuso.matriz[0], self.matriz[1] * numdifuso.matriz[1],
                                         self.matriz[2] * numdifuso.matriz[2], self.matriz[3] * numdifuso.matriz[3])
            else:
                numeroDif = NumeroDifuso(self.matriz[0] * numdifuso.matriz[0], self.matriz[1] * numdifuso.matriz[1],
                                         self.matriz[2] * numdifuso.matriz[2], -1)
        else:
            numeroDif = NumeroDifuso(self.matriz[0] * numdifuso.matriz[0], self.matriz[1] * numdifuso.matriz[1],
                                     self.matriz[2] * numdifuso.matriz[2], self.matriz[2] * numdifuso.matriz[2])

        return numeroDif

    # Método para dividir numero difuso
    def division(self, numdifuso):

        if len(numdifuso.matriz) <= 2 or len(numdifuso.matriz) > 4:
            self.matriz = [0, 0, 0]
            return "La matriz que quiere sumar debe de tener entre 3 y 4 elementos"

        for elemento in numdifuso.matriz:
            if elemento == 0:
                self.matriz = [0, 0, 0]
                return "Uno de los elementos es un cero"

        numdifuso_trans = NumeroDifuso(1 / numdifuso.matriz[0], 1 / numdifuso.matriz[1], 1 / numdifuso.matriz[2],
                                       1 / numdifuso.matriz[3])
        # Transformamos la matriz para que cada elemento tenga su inverso
        if len(numdifuso.matriz) == 3:
            numdifuso_trans = [1 / numdifuso.matriz[0], 1 / numdifuso.matriz[1], 1 / numdifuso.matriz[2]]

        return self.multiplicacion(numdifuso_trans)

    def tostring(self):
        print(self.matriz)

def opuesto (numdifuso):

    if len(numdifuso.matriz, ) > 3:
        return NumeroDifuso(-numdifuso.matriz[0], numdifuso.matriz[1], numdifuso.matriz[2], numdifuso.matriz[3])

    return NumeroDifuso(-numdifuso.matriz[0], numdifuso.matriz[1], numdifuso.matriz[2], -1)


numdif = NumeroDifuso(fac=1, b=2, c=3, d=-1)
numdif_secundario = NumeroDifuso(fac=1, b=2, c=3, d=4)

numdif_suma = numdif.suma(numdif_secundario)
numdif_suma.tostring()

numdif_resta = numdif.resta(numdif_secundario)
numdif_resta.tostring()

numdif_mult = numdif.multiplicacion(numdif_secundario)
numdif_mult.tostring()

numdif_inv = opuesto(numdif_secundario)
numdif_inv.tostring()

numdif_div = numdif.division(numdif_secundario)
numdif_div.tostring()