from ejercicios.ejercicio import Ejercicio
import random

class EjercicioTest(Ejercicio):
    """
    Clase que representa un ejercicio tipo test.

    En este ejercicio el usuario debe elegir la traducción correcta
    entre varias opciones.
    """

    def __init__(self, tarjeta, opciones):
        """
        Inicializa un ejercicio tipo test.

        Parámetros:
        tarjeta: Tarjeta
            Tarjeta que contiene la palabra y su traducción correcta.
        opciones: list
            Lista de posibles respuestas (incluyendo la correcta).
        """
        super().__init__(tarjeta)

        self.opciones = opciones
        random.shuffle(self.opciones)

    def mostrar(self):
        """
        Muestra el ejercicio y las opciones de respuesta.
        """

        print(f"Traduce la palabra: {self.tarjeta.palabra}")

        letras = ["A", "B", "C", "D"]

        for i, opcion in enumerate(self.opciones):
            print(f"{letras[i]}) {opcion}")

    def comprobar_respuesta(self, respuesta):
        """
        Comprueba si la respuesta elegida por el usuario es correcta.

        Parámetros:
        respuesta: str
            Letra de la opción elegida por el usuario (A, B, C o D).

        Devuelve:
        bool
            True si la respuesta es correcta, False si es incorrecta.
        """
        letras = ["A", "B", "C", "D"]

        indice = letras.index(respuesta.upper())

        self.respondido = True

        if self.opciones[indice] == self.tarjeta.traduccion:
            self.correcto = True
        else:
            self.correcto = False

        return self.correcto
