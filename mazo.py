from tarjeta import Tarjeta
import random

class Mazo:
    '''
    Representa un conjunto de tarjetas organizadas bajo un mismo nombre o temática. Permite añadir, eliminar y mezclar tarjetas, además de unir y comparar mazos mediante sobrecarga de operadores. Gestiona el contenido que se utilizará en los ejercicios.
    '''
    def __init__(self, nombre):
        self.nombre=nombre
        self._tarjetas=[]

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip()=="":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre=valor.strip()

    @property
    def tarjeta(self):
        return self._tarjetas.copy()

    def anadir_tarjeta(self, tarjeta):
        if not isinstance(tarjeta, Tarjeta):
            raise TypeError("El objeto debe ser de tipo Tarjeta")
        if tarjeta in self._tarjetas:
            raise ValueError("La tarjeta ya existe en el mazo")
        self._tarjetas.append(tarjeta)

    def eliminar_tarjeta(self, tarjeta):
        if tarjeta not in self._tarjetas:
            raise ValueError("La tarjeta no está en el mazo")
        self._tarjetas.remove(tarjeta)

    def mezclar_tarjetas(self):
        random.shuffle(self._tarjetas)

    def __add__(self, other):
        if not isinstance(other, Mazo):
            raise TypeError("Solo se pueden unir objetos de tipo Mazo")

        nuevo_mazo=Mazo(f"{self.nombre} + {other.nombre}")

        for tarjeta in self._tarjetas:
            nuevo_mazo.añadir_tarjeta(tarjeta)

        for tarjeta in other._tarjetas:
            if tarjeta not in nuevo_mazo._tarjetas:
                nuevo_mazo.añadir_tarjeta(tarjeta)
        return nuevo_mazo

    def __eq__(self, other):
        if not isinstance(other, Mazo):
            return False

        if len(self._tarjetas) != len(other._tarjetas):
            return False

        for tarjeta in self._tarjetas:
            if tarjeta not in other._tarjetas:
                return False
        return True

    def __len__(self):
        return len(self._tarjetas)

    def __str__(self):
        return (f"Mazo: {self.nombre}\n"
                f"Número de tarjetas: {len(self)}")

