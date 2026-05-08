"""Módulo para la generación de ejercicios.

Este módulo define la clase GeneradorEjercicios, encargada de generar
distintos tipos de ejercicios a partir de un mazo de tarjetas.

Clases:
    - GeneradorEjercicios
"""

import random
from ejercicios.ejercicio_escritura import EjercicioEscritura
from ejercicios.ejercicio_test import EjercicioTest


class GeneradorEjercicios:
    """
    Clase encargada de generar ejercicios a partir de un mazo.

    Atributos:
    ----------
    mazo: Mazo
        Mazo del que se obtienen las tarjetas para generar ejercicios.

    Métodos:
    -------
    __init__(mazo: Mazo) -> None
        Inicializa el generador con un mazo.

    generar_escritura() -> list[EjercicioEscritura]
        Genera una lista de ejercicios de escritura.

    generar_test() -> list[EjercicioTest]
        Genera una lista de ejercicios tipo test con opciones aleatorias.
    """

    def __init__(self, mazo):
        """
        Inicializa una instancia de la clase GeneradorEjercicios.

        Parámetros:
        ----------
        mazo: Mazo
            Mazo a partir del cual se generarán los ejercicios.
        """
        self.mazo = mazo

    def generar_escritura(self):
        """
        Genera una lista de ejercicios de escritura.

        Devuelve:
        --------
        list[EjercicioEscritura]
            Lista de ejercicios de escritura generados a partir del mazo.
        """
        return [EjercicioEscritura(t) for t in self.mazo.obtener_tarjetas()]

    def generar_test(self):
        """
        Genera una lista de ejercicios tipo test con opciones aleatorias.

        Devuelve:
        --------
        list[EjercicioTest]
            Lista de ejercicios tipo test generados a partir del mazo.
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