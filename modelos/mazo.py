"""Módulo que define la clase Mazo."""

from modelos.tarjeta import Tarjeta
import random


class Mazo:
    """
    Representa un conjunto de tarjetas agrupadas bajo un nombre.

    Atributos:
        nombre (str): Nombre del mazo.
        _tarjetas (list[Tarjeta]): Lista interna de tarjetas.
    """

    def __init__(self, nombre):
        """
        Inicializa el mazo.

        Parámetros:
            nombre (str): Nombre del mazo.
        """
        self.nombre = nombre
        self._tarjetas = []

    @property
    def nombre(self):
        """Devuelve el nombre del mazo."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre validando que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def tarjetas(self):
        """Devuelve una copia de las tarjetas."""
        return self._tarjetas.copy()

    def anadir_tarjeta(self, tarjeta):
        """
        Añade una tarjeta al mazo.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta a añadir.

        Lanza:
            TypeError: Si no es una Tarjeta.
            ValueError: Si ya existe.
        """
        if not isinstance(tarjeta, Tarjeta):
            raise TypeError("El objeto debe ser de tipo Tarjeta")
        if tarjeta in self._tarjetas:
            raise ValueError("La tarjeta ya existe en el mazo")
        self._tarjetas.append(tarjeta)

    def eliminar_tarjeta(self, tarjeta):
        """
        Elimina una tarjeta del mazo.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta a eliminar.

        Lanza:
            ValueError: Si no existe.
        """
        if tarjeta not in self._tarjetas:
            raise ValueError("La tarjeta no está en el mazo")
        self._tarjetas.remove(tarjeta)

    def mezclar_tarjetas(self):
        """Mezcla aleatoriamente las tarjetas."""
        random.shuffle(self._tarjetas)

    def __add__(self, other):
        """
        Une dos mazos en uno nuevo.

        Parámetros:
            other (Mazo): Mazo a combinar.

        Devuelve:
            Mazo: Nuevo mazo sin duplicados.
        """
        if not isinstance(other, Mazo):
            raise TypeError("Solo se pueden unir objetos de tipo Mazo")

        nuevo = Mazo(f"{self.nombre} + {other.nombre}")

        for tarjeta in self._tarjetas:
            nuevo.anadir_tarjeta(tarjeta)

        for tarjeta in other._tarjetas:
            if tarjeta not in nuevo._tarjetas:
                nuevo.anadir_tarjeta(tarjeta)

        return nuevo

    def __eq__(self, other):
        """
        Compara dos mazos por sus tarjetas.
        """
        if not isinstance(other, Mazo):
            return False
        return set(self._tarjetas) == set(other._tarjetas)

    def __len__(self):
        """Devuelve el número de tarjetas."""
        return len(self._tarjetas)

    def __str__(self):
        """Representación del mazo."""
        return f"Mazo: {self.nombre}\nNúmero de tarjetas: {len(self)}"