"""
Módulo para la gestión de ejercicios de práctica.

Este módulo define la clase abstracta `Ejercicio`, que representa un ejercicio práctico basado en una tarjeta.
Sirve como clase base para distintos tipos de ejercicios, como ejercicios de escritura o tipo test.

Clases:
    - Ejercicio
"""

from tarjeta import Tarjeta
from abc import ABC, abstractmethod


class Ejercicio(ABC):
    """
    Clase abstracta que representa un ejercicio basado en una tarjeta.

    Atributos:
    tarjeta : Tarjeta
        Objeto de la clase Tarjeta que contiene la palabra y su traducción.
    puntuacion : int o float
        Número de puntos que vale el ejercicio si se responde correctamente.
    respondido : bool
        Indica si el ejercicio ya ha sido respondido por el usuario.
    correcto : bool
        Indica si la respuesta dada por el usuario fue correcta.

    Métodos:
    __init__(tarjeta : Tarjeta, puntuacion : int = 1)
        Inicializa el ejercicio con una tarjeta y una puntuación.

    mostrar() -> None
        Muestra el enunciado del ejercicio al usuario.

    comprobar_respuesta(respuesta : str)
        Método abstracto que comprueba si la respuesta del usuario es correcta.

    obtener_puntuacion() -> int o float
        Devuelve la puntuación obtenida en el ejercicio.

    __str__() -> str
        Devuelve una representación en texto del ejercicio.
    """

    def __init__(self, tarjeta, puntuacion=1):
        """
        Inicializa una instancia de la clase Ejercicio.

        Parámetros:
        tarjeta : Tarjeta
            Tarjeta que se utilizará para generar el ejercicio.
        puntuacion : int o float
            Puntuación que vale el ejercicio si se responde correctamente.
        """
        self.tarjeta = tarjeta
        self.puntuacion = puntuacion
        self.respondido = False
        self.correcto = False

    @property
    def tarjeta(self):
        """
        Obtiene la tarjeta asociada al ejercicio.
        """
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, valor):
        """
        Establece la tarjeta del ejercicio validando que sea del tipo Tarjeta.
        """
        if not isinstance(valor, Tarjeta):
            raise TypeError('El objeto tiene que ser de tipo Tarjeta')
        self._tarjeta = valor

    @property
    def puntuacion(self):
        """
        Obtiene la puntuación del ejercicio.
        """
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, valor):
        """
        Establece la puntuación del ejercicio validando que sea de tipo numérico
        y mayor que 0.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError('La puntuación tiene que ser numérica')

        if valor <= 0:
            raise ValueError('La puntuación tiene que ser mayor que 0')

        self._puntuacion = valor

    def mostrar(self):
        """
        Muestra el enunciado del ejercicio.

        En este caso se pide al usuario que traduzca la palabra
        almacenada en la tarjeta.
        """
        print(f"Traduce la palabra: {self.tarjeta.palabra}")

    @abstractmethod
    def comprobar_respuesta(self, respuesta):
        """
        Método abstracto que comprueba si la respuesta del usuario es correcta.
        """
        pass

    def obtener_puntuacion(self):
        """
        Devuelve la puntuación obtenida en el ejercicio.

        Retorna:
        int o float
            Devuelve la puntuación del ejercicio si la respuesta fue correcta,
            o 0 en caso contrario.
        """
        if self.correcto:
            return self.puntuacion
        else:
            return 0

    def __str__(self):
        """
        Devuelve una representación en texto del ejercicio.
        Retorna:
        str
            Muestra el tipo de ejercicio y la palabra asociada.
        """
        return f"Ejercicio: traducir '{self.tarjeta.palabra}'"