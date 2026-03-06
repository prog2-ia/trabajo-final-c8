from tarjeta import Tarjeta
from abc import ABC, abstractmethod


class Ejercicio(ABC):

    def __init__(self, tarjeta, puntuacion=1):
        self.tarjeta=tarjeta
        self.puntuacion=puntuacion
        self.respondido=False
        self.correcto=False

    @property
    def tarjeta(self):
        return self._tarjeta
    @tarjeta.setter
    def tarjeta(self, valor):
        if not isinstance(valor, Tarjeta):
            raise TypeError('El objeto tiene que ser de tipo Tarjeta')
        self._tarjeta=valor

    @property
    def puntuacion(self):
        return self._puntuacion
    @puntuacion.setter
    def puntuacion(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('La puntuación tiene que ser numérica')
        if valor <=0:
            raise ValueError('La puntuación tiene que ser mayor que 0')
        self._puntuacion=valor

    def mostrar(self):
        print(f"Traduce la palabra: {self.tarjeta.palabra}")

    @abstractmethod
    def comprobar_respuesta(self, respuesta):
        pass

    def obtener_puntuacion(self):
        if self.correcto:
            return self.puntuacion
        else:
            return 0

    def __str__(self):
        return f"Ejercicio: traducir '{self.tarjeta.palabra}'"