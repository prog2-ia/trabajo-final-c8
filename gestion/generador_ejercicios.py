"""Módulo que define la clase GeneradorEjercicios."""

import random
from ejercicios.ejercicio_escritura import EjercicioEscritura
from ejercicios.ejercicio_test import EjercicioTest


class GeneradorEjercicios:
    """
    Genera ejercicios a partir de un mazo.

    Atributos:
        mazo (Mazo): Mazo de tarjetas.
    """

    def __init__(self, mazo):
        """
        Inicializa el generador.

        Parámetros:
            mazo (Mazo): Mazo base para los ejercicios.
        """
        self.mazo = mazo

    def generar_escritura(self):
        """
        Genera ejercicios de escritura.

        Devuelve:
            list[EjercicioEscritura]: Lista de ejercicios.
        """
        return [EjercicioEscritura(t) for t in self.mazo.obtener_tarjetas()]

    def generar_test(self):
        """
        Genera ejercicios tipo test.

        Devuelve:
            list[EjercicioTest]: Lista de ejercicios.
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