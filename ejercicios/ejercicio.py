"""Módulo que define la clase abstracta Ejercicio."""

from modelos.tarjeta import Tarjeta
from abc import ABC, abstractmethod


class Ejercicio(ABC):
    """
    Clase base para ejercicios de práctica basados en una tarjeta.

    Atributos:
        tarjeta (Tarjeta): Tarjeta asociada al ejercicio.
        puntuacion (int | float): Puntos del ejercicio.
        respondido (bool): Indica si se ha respondido.
        correcto (bool): Indica si la respuesta fue correcta.
    """

    def __init__(self, tarjeta, puntuacion=1):
        """
        Inicializa el ejercicio.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta del ejercicio.
            puntuacion (int | float): Valor del ejercicio.
        """
        self.tarjeta = tarjeta
        self.puntuacion = puntuacion
        self.respondido = False
        self.correcto = False

    @property
    def tarjeta(self):
        """Devuelve la tarjeta."""
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, valor):
        """Establece la tarjeta validando su tipo."""
        if not isinstance(valor, Tarjeta):
            raise TypeError("El objeto tiene que ser de tipo Tarjeta")
        self._tarjeta = valor

    @property
    def puntuacion(self):
        """Devuelve la puntuación."""
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, valor):
        """Establece la puntuación validando que sea positiva."""
        if not isinstance(valor, (int, float)):
            raise TypeError("La puntuación tiene que ser numérica")
        if valor <= 0:
            raise ValueError("La puntuación tiene que ser mayor que 0")
        self._puntuacion = valor

    def mostrar(self):
        """Muestra el enunciado del ejercicio."""
        print(f"Traduce la palabra: {self.tarjeta.palabra}")

    @abstractmethod
    def comprobar_respuesta(self, respuesta):
        """Comprueba si la respuesta es correcta."""
        pass

    def obtener_puntuacion(self):
        """
        Devuelve la puntuación obtenida.

        Devuelve:
            int | float: Puntos si es correcto, 0 si no.
        """
        return self.puntuacion if self.correcto else 0

    def __str__(self):
        """Representación del ejercicio."""
        return f"Ejercicio: traducir '{self.tarjeta.palabra}'"