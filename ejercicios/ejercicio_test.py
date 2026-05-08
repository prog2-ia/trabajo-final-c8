from ejercicios.ejercicio import Ejercicio
import random


class EjercicioTest(Ejercicio):
    """
    Ejercicio tipo test en el que se elige la traducción correcta.
    """

    def __init__(self, tarjeta, opciones):
        """
        Inicializa el ejercicio.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta del ejercicio.
            opciones (list): Lista de posibles respuestas.
        """
        super().__init__(tarjeta)
        self.opciones = opciones
        random.shuffle(self.opciones)

    def mostrar(self):
        """Muestra la palabra y las opciones."""
        print(f"Traduce la palabra: {self.tarjeta.palabra}")

        letras = ["A", "B", "C", "D"]
        for i, opcion in enumerate(self.opciones):
            print(f"{letras[i]}) {opcion}")

    def comprobar_respuesta(self, respuesta):
        """
        Comprueba si la opción elegida es correcta.

        Parámetros:
            respuesta (str): Letra seleccionada (A, B, C o D).

        Devuelve:
            bool: True si es correcta.
        """
        letras = ["A", "B", "C", "D"]
        indice = letras.index(respuesta.upper())

        self.respondido = True

        if self.opciones[indice] == self.tarjeta.traduccion:
            self.correcto = True
        else:
            self.correcto = False

        return self.correcto