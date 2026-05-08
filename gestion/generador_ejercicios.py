import random
from ejercicios.ejercicio_escritura import EjercicioEscritura
from ejercicios.ejercicio_test import EjercicioTest


class GeneradorEjercicios:
    """
    Clase encargada de generar ejercicios a partir de un mazo.
    """

    def __init__(self, mazo):
        self.mazo = mazo

    def generar_escritura(self):
        """
        Genera una lista de ejercicios de escritura.
        """
        return [EjercicioEscritura(t) for t in self.mazo.obtener_tarjetas()]

    def generar_test(self):
        """
        Genera una lista de ejercicios tipo test con opciones correctas y aleatorias.
        """
        ejercicios = []

        for tarjeta in self.mazo.obtener_tarjetas():

            opciones = [
                t.traduccion
                for t in self.mazo.obtener_tarjetas()
                if t != tarjeta
            ]

            random.shuffle(opciones)
            opciones = opciones[:3]
            opciones.append(tarjeta.traduccion)
            random.shuffle(opciones)

            ejercicios.append(EjercicioTest(tarjeta, opciones))

        return ejercicios