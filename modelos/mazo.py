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

    def __init__(self, nombre: str) -> None:
        """
        Inicializa el mazo.

        Parámetros:
            nombre (str): Nombre del mazo.
        """
        self.nombre = nombre
        self._tarjetas: list[Tarjeta] = []

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del mazo."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Establece el nombre validando que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def tarjetas(self) -> list[Tarjeta]:
        """Devuelve una copia de las tarjetas."""
        return self._tarjetas.copy()

    def anadir_tarjeta(self, tarjeta: Tarjeta) -> None:
        """
        Añade una tarjeta al mazo.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta a añadir.

        Lanza:
            TypeError: Si no es una Tarjeta.
            ValueError: Si ya existe en el mazo.
        """
        if not isinstance(tarjeta, Tarjeta):
            raise TypeError("El objeto debe ser de tipo Tarjeta.")
        if tarjeta in self._tarjetas:
            raise ValueError("La tarjeta ya existe en el mazo.")
        self._tarjetas.append(tarjeta)

    def eliminar_tarjeta(self, tarjeta: Tarjeta) -> None:
        """
        Elimina una tarjeta del mazo.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta a eliminar.

        Lanza:
            ValueError: Si no existe en el mazo.
        """
        if tarjeta not in self._tarjetas:
            raise ValueError("La tarjeta no está en el mazo.")
        self._tarjetas.remove(tarjeta)

    def mezclar_tarjetas(self) -> None:
        """Mezcla aleatoriamente las tarjetas."""
        random.shuffle(self._tarjetas)

    def __add__(self, other: "Mazo") -> "Mazo":
        """
        Une dos mazos en uno nuevo sin duplicados.

        Parámetros:
            other (Mazo): Mazo a combinar.

        Devuelve:
            Mazo: Nuevo mazo resultante.

        Lanza:
            TypeError: Si other no es un Mazo.
        """
        if not isinstance(other, Mazo):
            raise TypeError("Solo se pueden unir objetos de tipo Mazo.")

        nuevo = Mazo(f"{self.nombre} + {other.nombre}")
        for tarjeta in self._tarjetas:
            nuevo.anadir_tarjeta(tarjeta)
        for tarjeta in other._tarjetas:
            if tarjeta not in nuevo._tarjetas:
                nuevo.anadir_tarjeta(tarjeta)
        return nuevo

    def __eq__(self, other: object) -> bool:
        """Compara dos mazos por el conjunto de tarjetas."""
        if not isinstance(other, Mazo):
            return False
        return set(self._tarjetas) == set(other._tarjetas)

    def __len__(self) -> int:
        """Devuelve el número de tarjetas."""
        return len(self._tarjetas)

    def __str__(self) -> str:
        """Representación del mazo."""
        return f"Mazo: {self.nombre}\nNúmero de tarjetas: {len(self)}"